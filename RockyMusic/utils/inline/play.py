import math
from pyrogram.types import InlineKeyboardButton
from RockyMusic.utils.formatters import time_to_seconds

# Progress Bar Generator
def get_progress_bar(played_sec, total_sec):
    try:
        percentage = (played_sec / total_sec) * 100
    except ZeroDivisionError:
        percentage = 0
    umm = math.floor(percentage)

    if umm <= 0:
        bar = "✄·─·─·─·─·─·─·─·─·─"
    if 0 < umm <= 10:
        bar = "✄·─·─·─·─·─·─·─·─·─"
    elif 10 < umm < 20:
        bar = "-ˋˏ✄·─·─·─·─·─·─·─·─"
    elif 20 <= umm < 30:
        bar = "-ˋˏ-ˋˏ✄·─·─·─·─·─·─·─"
    elif 30 <= umm < 40:
        bar = "-ˋˏ-ˋˏ-ˋˏ✄·─·─·─·─·─·─"
    elif 40 <= umm < 50:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─·─·─·─"
    elif 50 <= umm < 60:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─·─·─"
    elif 60 <= umm < 70:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─·─"
    elif 70 <= umm < 80:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─·─"
    elif 80 <= umm < 95:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·─"
    else:
        bar = "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·"

    return bar

# Track Buttons
def track_markup(_, videoid, user_id, channel, fplay):
    return [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")
        ],
    ]

# Stream Buttons with Timer + Styled Buttons
def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    progress_bar = get_progress_bar(played_sec, duration_sec)

    return [
        [
            InlineKeyboardButton(text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {progress_bar} {dur}",
                url="https://t.me/NikkuXBot?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text="⌯ 𝐀ᴅᴅ 𝐌є ⌯", url="https://t.me/NikkuXBot?startgroup=true"),
            InlineKeyboardButton(text="⌯ 𝐎ᴡɴᴇʀ ⌯", url="https://t.me/+18624419123"),
        ],
    ]

# Stream Buttons without Timer
def stream_markup(_, chat_id):
    return [
        [
            InlineKeyboardButton(text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
    ]

# Playlist Buttons
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    return [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"AviaxPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"AviaxPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")
        ],
    ]

# LiveStream Buttons
def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    return [
        [
            InlineKeyboardButton(text=_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}")
        ],
    ]

# Slider Buttons
def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    return [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}"),
        ],
    ]

# Credit
# Modified with love by Nand Yaduwanshi @WTF_WhyMeeh
