# ケリー基準

このプロジェクトは、ケリー基準 を用いて最適な賭け金割合を計算し、
モンテカルロシミュレーションで資金の推移を可視化する分析環境です。

# 環境構築

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
jupyter notebook notebooks/01_kelly.ipynb
```
