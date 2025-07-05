import streamlit as st
import matplotlib.pyplot as plt
import calendar

# 閉室日（ジムが休みの日）
closed_dates = {
    (2025, 4): [20], (2025, 5): [11], (2025, 6): [22], (2025, 7): [20],
    (2025, 8): [8, 9, 10, 11], (2025, 9): [14], (2025, 10): [5],
    (2025, 11): [23], (2025, 12): [21, 29, 30, 31],
    (2026, 1): [1, 2, 3, 4, 5], (2026, 2): [1], (2026, 3): [15],
}

# 開室日を取得する関数
def get_open_days(year, month):
    _, num_days = calendar.monthrange(year, month)
    all_days = set(range(1, num_days + 1))
    closed = set(closed_dates.get((year, month), []))
    return sorted(list(all_days - closed))

# カレンダー全体を描く関数
def draw_academic_year_calendar():
    fig, axs = plt.subplots(4, 3, figsize=(16, 12))
    plt.subplots_adjust(hspace=0.6)

    months = [(2025, m) for m in range(4, 13)] + [(2026, m) for m in range(1, 4)]
    month_labels = ['April', 'May', 'June', 'July', 'August', 'September',
                    'October', 'November', 'December', 'January', 'February', 'March']

    for idx, ax in enumerate(axs.flat):
        year, month = months[idx]
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        ax.set_title(f"{year} {month_labels[idx]}", fontsize=14)

        for i, day_name in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
            ax.text(i, 6, day_name, ha='center', va='center', fontsize=10, weight='bold')

        open_days = get_open_days(year, month)
        for week_num, week in enumerate(month_days):
            for day_idx, day in enumerate(week):
                if day != 0:
                    y = 5 - week_num
                    ax.text(day_idx, y, str(day), ha='center', va='center', fontsize=10)
                    if day in open_days:
                        circle = plt.Circle((day_idx, y), 0.35, color='green', fill=False, linewidth=1.5)
                        ax.add_patch(circle)

        ax.set_xlim(-0.5, 6.5)
        ax.set_ylim(-0.5, 6.5)
        ax.axis('off')

    return fig

# Streamlit画面構成
st.title("🏋️‍♂️ 早稲田ジム開室カレンダー（2025年度）")
st.write("○がついている日が開室日です。閉室日は内部に登録済みです。")
fig = draw_academic_year_calendar()
st.pyplot(fig)
