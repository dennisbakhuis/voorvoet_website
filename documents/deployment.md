# Deployment Guide: Reflex Website to VPS

This document describes the complete deployment process for deploying this Reflex website to a Virtual Private Server (VPS), including both production and development environments.

## Table of Contents

1. [VPS Setup](#1-vps-setup)
2. [Initial Server Configuration](#2-initial-server-configuration)
3. [SSL Certificate Setup (Cloudflare)](#3-ssl-certificate-setup-cloudflare)
4. [DNS Configuration](#4-dns-configuration)
5. [Nginx Configuration](#5-nginx-configuration)
6. [Application Setup](#6-application-setup)
7. [Systemd Services](#7-systemd-services)
8. [Webhook Configuration](#8-webhook-configuration)
9. [Deployment Scripts](#9-deployment-scripts)

---

## 1. VPS Setup

### Provider
- **Provider**: [Etheron](https://etheron.nl/servers/vps)
- **Plan**: Tiny server (~EUR 32/year)
- **OS**: Ubuntu Server 2024 LTS
- **Authentication**: SSH key

### SSH Key Generation

Generate an SSH key pair:

```bash
ssh-keygen -t ed25519 -C "<your_email_as_a_label>" -f ~/.ssh/id_ed25519_etheron
```

Copy the contents of `id_ed25519_etheron.pub` and add it during VPS provisioning.

### SSH Configuration

Add to your local `~/.ssh/config`:

```ssh-config
Host etheron
  HostName <your-vps-ip>
  User root
  IdentityFile ~/.ssh/id_ed25519_etheron
  IdentitiesOnly yes
```

Connect to your VPS:

```bash
ssh etheron
```

---

## 2. Initial Server Configuration

### System Updates and Package Installation

Update the system and install required packages:

```bash
apt update && apt upgrade -y
apt install webhook nginx ufw curl git unzip -y
curl -LsSf https://astral.sh/uv/install.sh | sh
```

The packages installed are:
- **webhook**: Listens for HTTP webhooks and executes commands (for automated deployments)
- **nginx**: Web server and reverse proxy
- **ufw**: Uncomplicated Firewall for managing firewall rules
- **curl, git, unzip**: Standard utilities for downloading and managing code
- **uv**: Fast Python package installer and virtual environment manager

### Firewall Configuration

Configure the firewall to allow only necessary traffic:

```bash
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp

ufw enable
ufw status
```

This opens ports for SSH (22), HTTP (80), and HTTPS (443) while blocking all other incoming traffic.

---

## 3. SSL Certificate Setup (Cloudflare)

### Generate Cloudflare Origin Certificate

1. Log into Cloudflare dashboard
2. Select your domain
3. Navigate to **SSL/TLS → Origin Server**
4. Click **Create Certificate**
5. Configure settings:
   - **Private key type**: RSA (2048)
   - **Hostnames**: `yourdomain.com` and `*.yourdomain.com`
   - **Certificate Validity**: 15 years
6. Click **Create**

You'll receive two files:
- Origin Certificate (begins with `-----BEGIN CERTIFICATE-----`)
- Private Key (begins with `-----BEGIN PRIVATE KEY-----`)

### Save Certificate on VPS

Create directory structure:

```bash
mkdir -p /etc/ssl/cloudflare/yourdomain.com
```

Save the certificate:

```bash
vi /etc/ssl/cloudflare/yourdomain.com/cert.pem
```

Press `i` to enter insert mode, paste the Origin Certificate from Cloudflare, then press `Esc`, type `:wq`, and press `Enter` to save and exit.

Save the private key:

```bash
vi /etc/ssl/cloudflare/yourdomain.com/key.pem
```

Press `i` to enter insert mode, paste the Private Key from Cloudflare, then press `Esc`, type `:wq`, and press `Enter` to save and exit.

Set proper permissions:

```bash
chmod 600 /etc/ssl/cloudflare/yourdomain.com/key.pem
chmod 644 /etc/ssl/cloudflare/yourdomain.com/cert.pem
```

---

## 4. DNS Configuration

### Cloudflare DNS Records

In Cloudflare dashboard, navigate to **DNS → Records**:

**Main domain A record:**
- **Type**: A
- **Name**: @
- **IPv4 address**: `<your-vps-ip>`
- **Proxy status**: Proxied (orange cloud)
- **TTL**: Auto

**WWW subdomain A record:**
- **Type**: A
- **Name**: www
- **IPv4 address**: `<your-vps-ip>`
- **Proxy status**: Proxied (orange cloud)
- **TTL**: Auto

**Dev subdomain A record:**
- **Type**: A
- **Name**: dev
- **IPv4 address**: `<your-vps-ip>`
- **Proxy status**: Proxied (orange cloud)
- **TTL**: Auto

**Deploy subdomain A record (for webhooks):**
- **Type**: A
- **Name**: deploy
- **IPv4 address**: `<your-vps-ip>`
- **Proxy status**: Proxied (orange cloud)
- **TTL**: Auto

### SSL/TLS Settings

Navigate to **SSL/TLS → Overview**:
- Set encryption mode to: **Full (strict)**

---

## 5. Nginx Configuration

Nginx acts as a reverse proxy, routing incoming HTTPS traffic to the appropriate Reflex application (production or development) and handling SSL/TLS termination. It also routes webhook requests to the webhook service.

### Create Nginx Site Configuration

Create the Nginx configuration file:

```bash
vi /etc/nginx/sites-available/voorvoeten.nl.conf
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name voorvoeten.nl www.voorvoeten.nl;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name voorvoeten.nl www.voorvoeten.nl;

    ssl_certificate /etc/ssl/cloudflare/voorvoeten.nl/cert.pem;
    ssl_certificate_key /etc/ssl/cloudflare/voorvoeten.nl/key.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    access_log /var/www/voorvoeten.nl/logs/access.log;
    error_log /var/www/voorvoeten.nl/logs/error.log;

    location /api/ {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /_event {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location / {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    server_name dev.voorvoeten.nl;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name dev.voorvoeten.nl;

    ssl_certificate /etc/ssl/cloudflare/voorvoeten.nl/cert.pem;
    ssl_certificate_key /etc/ssl/cloudflare/voorvoeten.nl/key.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    access_log /var/www/dev.voorvoeten.nl/logs/access.log;
    error_log /var/www/dev.voorvoeten.nl/logs/error.log;

    location /api/ {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /_event {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location / {
        proxy_pass http://localhost:8001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 443 ssl http2;
    server_name deploy.voorvoeten.nl;

    ssl_certificate /etc/ssl/cloudflare/voorvoeten.nl/cert.pem;
    ssl_certificate_key /etc/ssl/cloudflare/voorvoeten.nl/key.pem;

    location /hooks/ {
        proxy_pass http://localhost:9000/hooks/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

This configuration defines three server blocks:

**Production site (voorvoeten.nl):**
- Redirects HTTP to HTTPS
- Proxies `/api/` requests to backend on port 3000
- Proxies `/_event` (WebSocket) to backend on port 3000
- Proxies all other requests to frontend on port 8000
- Logs access and errors to production logs directory

**Development site (dev.voorvoeten.nl):**
- Same structure as production but uses ports 3001 and 8001
- Separate logs in the development directory

**Webhook endpoint (deploy.voorvoeten.nl):**
- Proxies webhook requests to the webhook service on port 9000
- Accessible at `https://deploy.voorvoeten.nl/hooks/deploy-prod` and `https://deploy.voorvoeten.nl/hooks/deploy-dev`

### Enable the Site

Create a symbolic link to enable the site:

```bash
ln -s /etc/nginx/sites-available/voorvoeten.nl.conf /etc/nginx/sites-enabled/
```

### Test Nginx Configuration

Verify the configuration syntax is correct:

```bash
nginx -t
```

You should see output indicating the configuration is valid. If there are errors, review the configuration file for typos.

### Restart Nginx

Apply the configuration by restarting Nginx:

```bash
systemctl restart nginx
```

Verify Nginx is running:

```bash
systemctl status nginx
```

---

## 6. Application Setup

This section sets up the Reflex application in two separate environments: production and development. Each environment will run independently with its own codebase, configuration, and logs.

### Directory Structure

The application will be organized as follows:
- `/var/www/voorvoeten.nl/` - Production environment
  - `app/` - Contains the application code
  - `logs/` - Contains application and deployment logs
- `/var/www/dev.voorvoeten.nl/` - Development environment (same structure)

### Production Environment Setup

Create the directory structure and clone the repository:

```bash
mkdir -p /var/www/voorvoeten.nl/{app,logs}
cd /var/www/voorvoeten.nl/app
git clone https://github.com/dennisbakhuis/voorvoet_website.git
cd voorvoet_website
uv sync
```

The `uv sync` command installs all Python dependencies defined in the project.

### Development Environment Setup

Create a separate environment for development with the dev branch:

```bash
mkdir -p /var/www/dev.voorvoeten.nl/{app,logs}
cd /var/www/dev.voorvoeten.nl/app
git clone https://github.com/dennisbakhuis/voorvoet_website.git
cd voorvoet_website
git checkout dev
uv sync
```

The development environment tracks the `dev` branch, allowing you to test changes before deploying to production.

---

## 7. Systemd Services

Systemd services allow the Reflex applications to run continuously in the background, automatically restart on failure, and start on system boot. We'll create two services: one for production and one for development.

### Production Service

Create the systemd service file for production:

```bash
vi /etc/systemd/system/reflex-voorvoeten-prod.service
```

Add the following configuration:

```ini
[Unit]
Description=Reflex App - voorvoeten.nl
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/var/www/voorvoeten.nl/app/voorvoet_website
ExecStart=/root/.local/bin/uv run reflex run --env prod --backend-port 3000 --frontend-port 8000
Restart=always
RestartSec=10

StandardOutput=append:/var/www/voorvoeten.nl/logs/app.log
StandardError=append:/var/www/voorvoeten.nl/logs/error.log

[Install]
WantedBy=multi-user.target
```

Key configuration points:
- The service runs the Reflex app on ports 3000 (backend) and 8000 (frontend)
- It automatically restarts if it crashes, waiting 10 seconds between attempts
- Logs are written to the logs directory

### Development Service

Create the systemd service file for development:

```bash
vi /etc/systemd/system/reflex-voorvoeten-dev.service
```

Add the following configuration:

```ini
[Unit]
Description=Reflex App - dev.voorvoeten.nl
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/var/www/dev.voorvoeten.nl/app/voorvoet_website
ExecStart=/root/.local/bin/uv run reflex run --env prod --backend-port 3001 --frontend-port 8001
Restart=always
RestartSec=10

StandardOutput=append:/var/www/dev.voorvoeten.nl/logs/app.log
StandardError=append:/var/www/dev.voorvoeten.nl/logs/error.log

[Install]
WantedBy=multi-user.target
```

Note that the development environment uses different ports (3001 and 8001) to avoid conflicts with production.

### Enable and Start Services

Reload systemd to recognize the new services:

```bash
systemctl daemon-reload
```

Enable both services to start automatically on system boot:

```bash
systemctl enable reflex-voorvoeten-prod.service
systemctl enable reflex-voorvoeten-dev.service
```

Start both services:

```bash
systemctl start reflex-voorvoeten-prod.service
systemctl start reflex-voorvoeten-dev.service
```

Verify that both services are running:

```bash
systemctl status reflex-voorvoeten-prod.service
systemctl status reflex-voorvoeten-dev.service
```

You should see "active (running)" in the output for both services.

---

## 8. Webhook Configuration

Webhooks enable automated deployments. When you push code to GitHub, you can configure GitHub Actions or other CI/CD tools to send an HTTP request to your server, which then triggers the deployment script. The webhook service listens for these requests and executes the appropriate deployment script based on authentication and the webhook ID.

### Webhook Service

First, create the systemd service that will run the webhook listener:

```bash
vi /etc/systemd/system/webhook.service
```

Add the following configuration:

```ini
[Unit]
Description=Webhook Service
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/webhook -hooks /etc/webhook/hooks.json -port 9000 -verbose
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

This service listens on port 9000 for incoming webhook requests.

### Webhook Hooks Configuration

Create the directory for webhook configuration:

```bash
mkdir -p /etc/webhook
```

Create the hooks configuration file:

```bash
vi /etc/webhook/hooks.json
```

Add the webhook definitions:

```json
[
  {
    "id": "deploy-prod",
    "execute-command": "/var/www/scripts/deploy-voorvoeten-prod.sh",
    "command-working-directory": "/var/www/voorvoeten.nl/app/voorvoet_website",
    "response-message": "Production deployment started",
    "pass-arguments-to-command": [],
    "trigger-rule": {
      "match": {
        "type": "value",
        "value": "<secret_key>",
        "parameter": {
          "source": "header",
          "name": "X-Webhook-Token"
        }
      }
    }
  },
  {
    "id": "deploy-dev",
    "execute-command": "/var/www/scripts/deploy-voorvoeten-dev.sh",
    "command-working-directory": "/var/www/dev.voorvoeten.nl/app/voorvoet_website",
    "response-message": "Development deployment started",
    "pass-arguments-to-command": [],
    "trigger-rule": {
      "match": {
        "type": "value",
        "value": "<secret_key>",
        "parameter": {
          "source": "header",
          "name": "X-Webhook-Token"
        }
      }
    }
  }
]
```

Important: Replace `<secret_key>` with a secure random token. This token must be included in the `X-Webhook-Token` header of webhook requests for authentication. You can generate a secure token with: `openssl rand -hex 32`

The configuration defines two webhook endpoints:
- `deploy-prod`: Triggers production deployment when accessed at `/hooks/deploy-prod`
- `deploy-dev`: Triggers development deployment when accessed at `/hooks/deploy-dev`

### Enable Webhook Service

Reload systemd and start the webhook service:

```bash
systemctl daemon-reload
systemctl enable webhook.service
systemctl start webhook.service
```

Verify the webhook service is running:

```bash
systemctl status webhook.service
```

---

## 9. Deployment Scripts

The deployment scripts automate the process of updating the application when new code is pushed to GitHub. Each script pulls the latest code from the appropriate Git branch, installs any new dependencies, and restarts the service. All deployment actions are logged for troubleshooting.

### Create Scripts Directory

Create a central location for deployment scripts:

```bash
mkdir -p /var/www/scripts
```

### Production Deployment Script

Create the production deployment script:

```bash
vi /var/www/scripts/deploy-voorvoeten-prod.sh
```

Add the following script content:

```bash
#!/bin/bash

REPO_DIR="/var/www/voorvoeten.nl/app/voorvoet_website"
SERVICE_NAME="reflex-voorvoeten-prod.service"
LOG_FILE="/var/www/voorvoeten.nl/logs/deploy.log"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

log_message "Starting production deployment..."

cd "$REPO_DIR" || exit 1

git fetch origin
git checkout main
git pull origin main

log_message "Installing dependencies..."
/root/.local/bin/uv sync

log_message "Restarting service..."
systemctl restart "$SERVICE_NAME"

if systemctl is-active --quiet "$SERVICE_NAME"; then
    log_message "Deployment successful! Service is running."
else
    log_message "Deployment failed! Service is not running."
    exit 1
fi

log_message "Production deployment completed."
```

This script performs the following steps:
1. Navigates to the production repository directory
2. Fetches the latest changes from GitHub
3. Checks out and pulls the `main` branch
4. Installs or updates Python dependencies using `uv sync`
5. Restarts the production systemd service
6. Verifies the service started successfully
7. Logs all actions with timestamps to `/var/www/voorvoeten.nl/logs/deploy.log`

### Development Deployment Script

Create the development deployment script:

```bash
vi /var/www/scripts/deploy-voorvoeten-dev.sh
```

Add the following script content:

```bash
#!/bin/bash

REPO_DIR="/var/www/dev.voorvoeten.nl/app/voorvoet_website"
SERVICE_NAME="reflex-voorvoeten-dev.service"
LOG_FILE="/var/www/dev.voorvoeten.nl/logs/deploy.log"

log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

log_message "Starting development deployment..."

cd "$REPO_DIR" || exit 1

git fetch origin
git checkout dev
git pull origin dev

log_message "Installing dependencies..."
/root/.local/bin/uv sync

log_message "Restarting service..."
systemctl restart "$SERVICE_NAME"

if systemctl is-active --quiet "$SERVICE_NAME"; then
    log_message "Deployment successful! Service is running."
else
    log_message "Deployment failed! Service is not running."
    exit 1
fi

log_message "Development deployment completed."
```

This script is identical to the production script except it works with the `dev` branch and the development environment paths.

### Make Scripts Executable

Both scripts need execute permissions to be run by the webhook service:

```bash
chmod +x /var/www/scripts/deploy-voorvoeten-prod.sh
chmod +x /var/www/scripts/deploy-voorvoeten-dev.sh
```

You can now trigger deployments by calling the webhook endpoints or by manually running these scripts.

---

## Verification

After completing the setup, verify that all services are running correctly and can be managed properly.

### Check Service Status

Verify that all three services are active and running:

```bash
systemctl status reflex-voorvoeten-prod.service
systemctl status reflex-voorvoeten-dev.service
systemctl status webhook.service
```

Each service should show "active (running)" in green. If any service shows "failed" or "inactive", check the troubleshooting section below.

### View Application Logs

Monitor the application logs in real-time to see requests and application output:

```bash
tail -f /var/www/voorvoeten.nl/logs/app.log
tail -f /var/www/dev.voorvoeten.nl/logs/app.log
```

### View Deployment Logs

Check deployment logs to see the history of deployments and their status:

```bash
tail -f /var/www/voorvoeten.nl/logs/deploy.log
tail -f /var/www/dev.voorvoeten.nl/logs/deploy.log
```

### View Error Logs

Monitor error logs to identify any issues with the application:

```bash
tail -f /var/www/voorvoeten.nl/logs/error.log
tail -f /var/www/dev.voorvoeten.nl/logs/error.log
```

### Test Webhook Endpoints

Test the webhook functionality by manually triggering a deployment. Replace `<secret_key>` with the token you configured in the hooks.json file:

```bash
curl -X POST http://localhost:9000/hooks/deploy-dev \
  -H "X-Webhook-Token: <secret_key>"

curl -X POST http://localhost:9000/hooks/deploy-prod \
  -H "X-Webhook-Token: <secret_key>"
```

If successful, you should see "Development deployment started" or "Production deployment started" in the response, and you can watch the deployment progress in the deployment logs.

---

## Troubleshooting

Common issues and their solutions:

### Service Won't Start

If a Reflex service fails to start, check the systemd logs for detailed error messages:

```bash
journalctl -u reflex-voorvoeten-prod.service -n 50
journalctl -u reflex-voorvoeten-dev.service -n 50
```

Look for error messages about missing dependencies, configuration issues, or port conflicts. The last 50 lines usually contain the relevant error information.

### Port Already in Use

If you see errors about ports being in use, identify which process is using the port:

```bash
lsof -i :3000
lsof -i :8000
lsof -i :3001
lsof -i :8001
```

If another instance of the service is running, you may need to stop it:

```bash
systemctl stop reflex-voorvoeten-prod.service
systemctl stop reflex-voorvoeten-dev.service
```

Then start the service again.

### Git Pull Fails

If deployment fails due to Git errors, check the repository status and branch:

```bash
cd /var/www/voorvoeten.nl/app/voorvoet_website
git status
git branch -a
```

Common issues include:
- **Uncommitted local changes**: Reset to remote state with `git reset --hard origin/main`
- **Wrong branch**: Switch to correct branch with `git checkout main` or `git checkout dev`
- **Permission issues**: Ensure the repository directory is owned by the correct user

### Webhook Not Triggering

If webhooks aren't executing deployments, check the webhook service logs:

```bash
journalctl -u webhook.service -f
```

Common issues include:
- **Wrong secret key**: Verify the `X-Webhook-Token` header matches the value in `/etc/webhook/hooks.json`
- **Service not running**: Check `systemctl status webhook.service`
- **Firewall blocking port 9000**: If calling from external sources, ensure your firewall or Nginx is configured to forward requests to port 9000

### Application Not Accessible

If the Reflex application is running but not accessible:

1. Check if the service is actually running: `systemctl status reflex-voorvoeten-prod.service`
2. Verify the ports are listening: `netstat -tulpn | grep -E ':(3000|8000|3001|8001)'`
3. Check Nginx configuration if you're using it as a reverse proxy
4. Verify firewall rules allow HTTP/HTTPS traffic

### Viewing Real-Time Service Output

To see live output from a service (useful for debugging startup issues):

```bash
journalctl -u reflex-voorvoeten-prod.service -f
journalctl -u reflex-voorvoeten-dev.service -f
```

Press `Ctrl+C` to stop following the logs.
