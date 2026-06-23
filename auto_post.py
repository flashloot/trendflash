name: Auto Post News
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        # 強制更新 google-generativeai 到最新版
        run: pip install -U google-generativeai
      - name: Run Auto Script
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python auto_post.py
      - name: Commit changes
        run: |
          git config --global user.name "GitHub Action"
          git config --global user.email "action@github.com"
          git add .
          git commit -m "Auto Update News"
          git push
