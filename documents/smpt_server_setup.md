# Proton Mail SMTP Setup Guide

## Overview
This website uses Proton Mail SMTP to send contact form emails. The contact form collects user inquiries and sends them via SMTP to your specified notification email.

## Setup Steps

### 1. Create Proton Mail Account
- Sign up at [proton.me](https://proton.me) if you don't have an account
- Use a paid plan (required for SMTP/IMAP access)

### 2. Generate App Password
Proton requires app-specific passwords for SMTP access:

1. Log into Proton Mail
2. Go to **Settings** → **All Settings** → **Security and privacy**
3. Scroll to **App passwords** section
4. Click **Create app password**
5. Name it (e.g., "VoorVoet Website")
6. Copy the generated password (you won't see it again)

Official guide: https://proton.me/support/smtp-submission

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and update these values:

```bash
# SMTP Configuration
SMTP_HOST=smtp.protonmail.ch
SMTP_PORT=587
SMTP_USERNAME=your_proton_email@proton.me
SMTP_PASSWORD=your_app_password_from_step_2
SMTP_FROM_EMAIL=your_proton_email@proton.me
SMTP_TO_EMAIL=your_notification_email@example.com
```

**Settings explanation:**
- `SMTP_HOST`: Proton's SMTP server (always `smtp.protonmail.ch`)
- `SMTP_PORT`: Use port 587 (STARTTLS)
- `SMTP_USERNAME`: Your Proton email address
- `SMTP_PASSWORD`: The app password from step 2 (NOT your account password)
- `SMTP_FROM_EMAIL`: Same as username (sender address)
- `SMTP_TO_EMAIL`: Where you want to receive contact form submissions

### 4. Test the Configuration
1. Start the website: `uv run reflex run`
2. Navigate to the contact page
3. Fill out and submit the contact form
4. Check `SMTP_TO_EMAIL` inbox for the message
