# URL Shortener

A simple URL shortener service built with Flask. This service receives a URL and shortens it using a third-party API.

## Overview

This project provides a basic implementation of a URL shortener using Flask. Users can submit a URL to the API endpoint, which will then return a shortened version of the URL using an external shortening service.

## Features

- Receives a URL via a POST request.
- Shortens the URL using a third-party API.
- Returns the shortened URL.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/url-shortener.git

    Navigate to the Project Directory

    bash

cd url-shortener

Create a Virtual Environment (Optional but recommended)

bash

python -m venv venv

Activate the Virtual Environment

    On Windows:

    bash

venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install the Required Packages

bash

    pip install -r requirements.txt

Usage

    Start the Flask Application

    bash

python app.py

Send a POST Request to Shorten a URL

Use a tool like curl or Postman to send a POST request to http://localhost:5000/shorten with the following JSON body:

json

{
  "url": "https://www.example.com"
}

Receive the Shortened URL

The response will include the shortened URL:

json

    {
      "short_url": "https://short.url/abcd1234"
    }

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For larger changes, please open an issue to discuss them first.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Authors

    Your Name - yourgithubprofile

Acknowledgements

    Thank you to the URL shortening service provider for their API.

راهنمای فارسی
معرفی

این پروژه یک سرویس کوتاه‌کننده URL ساده است که با استفاده از فریم‌ورک Flask پیاده‌سازی شده است. کاربران می‌توانند URL را به انتهای API ارسال کنند و نسخه کوتاه‌شده آن را دریافت کنند.
ویژگی‌ها

    دریافت URL از طریق درخواست POST.
    کوتاه کردن URL با استفاده از API یک سرویس خارجی.
    برگرداندن URL کوتاه‌شده.

نصب و راه‌اندازی

برای شروع با این پروژه، مراحل زیر را دنبال کنید:

    کپی کردن مخزن

    bash

git clone https://github.com/yourusername/url-shortener.git

رفتن به دایرکتوری پروژه

bash

cd url-shortener

ایجاد محیط مجازی (اختیاری ولی توصیه‌شده)

bash

python -m venv venv

فعال کردن محیط مجازی

    در ویندوز:

    bash

venv\Scripts\activate

در macOS/Linux:

bash

    source venv/bin/activate

نصب پکیج‌های مورد نیاز

bash

    pip install -r requirements.txt

استفاده

    اجرای برنامه Flask

    bash

python app.py

ارسال درخواست POST برای کوتاه کردن یک URL

از ابزاری مانند curl یا Postman برای ارسال درخواست POST به http://localhost:5000/shorten با بدنه JSON زیر استفاده کنید:

json

{
  "url": "https://www.example.com"
}

دریافت URL کوتاه‌شده

پاسخ شامل URL کوتاه‌شده خواهد بود:

json

    {
      "short_url": "https://short.url/abcd1234"
    }

مشارکت

مشارکت‌ها خوش‌آمدید! لطفاً مخزن را فورک کرده و تغییرات خود را با ارسال درخواست Pull به اشتراک بگذارید. برای تغییرات بزرگتر، لطفاً یک Issue باز کنید تا ابتدا درباره آن بحث کنیم.
مجوز

این پروژه تحت مجوز MIT منتشر شده است - جزئیات را در فایل LICENSE مشاهده کنید.
نویسندگان

    نام شما - پروفایل گیت‌هاب شما

قدردانی

    از ارائه‌دهنده API سرویس کوتاه‌کننده URL برای API آن تشکر می‌کنیم.
