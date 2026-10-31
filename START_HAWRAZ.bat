@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py launch_hawraz.py
  goto :eof
)
where python >nul 2>nul
if %errorlevel%==0 (
  python launch_hawraz.py
  goto :eof
)
echo Python 3 روی این دستگاه پیدا نشد.
echo برای اجرای برنامه، Python 3 را نصب کن و دوباره این فایل را اجرا کن.
pause
