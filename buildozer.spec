name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y python3-pip build-essential git openjdk-17-jdk unzip zip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libstdc++6 patchelf

      - name: Install Buildozer
        run: |
          pip install --upgrade pip
          pip install buildozer cython==0.29.33

      - name: Build with Buildozer
        run: |
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: habesha-live-apk
          path: bin/*.apk
