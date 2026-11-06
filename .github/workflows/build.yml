name: APK Builder Worker

on:
  schedule:
    - cron: '*/15 * * * *' # هر ۱۵ دقیقه اجرا میشه
  workflow_dispatch: # دکمه اجرای دستی

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Java & System Tools
        run: |
          sudo apt-get update
          sudo apt-get install -y openjdk-17-jdk wget unzip
          
      - name: Install Python Requirements
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Setup Android SDK & Apktool
        run: |
          wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O sdk.zip
          unzip sdk.zip -d /opt/android-sdk/
          mkdir -p /opt/android-sdk/cmdline-tools/latest
          mv /opt/android-sdk/cmdline-tools/* /opt/android-sdk/cmdline-tools/latest/ || true
          echo "y" | /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager "build-tools;34.0.0"
          
          sudo ln -s /opt/android-sdk/build-tools/34.0.0/zipalign /usr/local/bin/zipalign
          sudo ln -s /opt/android-sdk/build-tools/34.0.0/apksigner /usr/local/bin/apksigner
          
          wget https://github.com/iBotPeaches/Apktool/releases/download/v2.9.3/apktool_2.9.3.jar -O /usr/local/bin/apktool.jar
          echo '#!/bin/sh' | sudo tee /usr/local/bin/apktool
          echo 'exec java -jar /usr/local/bin/apktool.jar "$@"' | sudo tee -a /usr/local/bin/apktool
          sudo chmod +x /usr/local/bin/apktool

      - name: Run Worker
        run: python worker.py
