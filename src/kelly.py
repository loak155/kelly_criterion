import numpy as np


def kelly_fraction(win_prob: float, odds: float) -> float:
    """
    ケリー基準による最適ベット率を計算する

    Args:
        win_prob (float): 勝率（0〜1）
        odds (float): オッズ（倍率）

    Returns:
        float: 資金に対する最適ベット率（負の場合は0を返す）

    Raises:
        ValueError: win_probが0〜1の範囲外、またはoddsが1以下の場合
    """
    if not (0 <= win_prob <= 1):
        raise ValueError(f"Invalid win_prob: {win_prob}. Must be between 0 and 1.")
    if odds <= 1:
        raise ValueError(f"Invalid odds: {odds}. Must be greater than 1.")

    net_odds = odds - 1
    lose_prob = 1 - win_prob

    optimal_fraction = (net_odds * win_prob - lose_prob) / net_odds
    return max(optimal_fraction, 0.0)


def simulate_kelly(
    start_capital: float,
    win_prob: float,
    win_odds: float,
    n_trials: int,
    fraction: float | None = None
) -> np.ndarray:
    """
    ケリー基準または指定割合で資金推移をモンテカルロシミュレーションする。

    Args:
        start_capital (float): 初期資金
        win_prob (float): 勝率（0〜1）
        win_odds (float): 払戻倍率（オッズ）
        n_trials (int): 試行回数
        fraction (float, optional): 賭ける割合。Noneの場合はケリー基準を使用。

    Returns:
        np.ndarray: 各試行後の資金履歴
    """
    # 入力チェック
    if start_capital <= 0:
        raise ValueError("start_capital must be positive")
    if not (0 <= win_prob <= 1):
        raise ValueError("win_prob must be between 0 and 1")
    if win_odds <= 1:
        raise ValueError("win_odds must be greater than 1")
    if n_trials < 1:
        raise ValueError("n_trials must be >= 1")

    if fraction is None:
        fraction = kelly_fraction(win_prob, win_odds)

    capital = start_capital
    history = [capital]

    net_odds = win_odds - 1

    for _ in range(n_trials):
        outcome = np.random.rand() < win_prob  # Trueなら勝ち
        if outcome:
            capital += capital * fraction * net_odds
        else:
            capital -= capital * fraction
        history.append(capital)

    return np.array(history)
