import sqlite3
from typing import Optional

DB_PATH = "course_bot.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id        INTEGER PRIMARY KEY,
            username       TEXT,
            full_name      TEXT NOT NULL,
            current_lesson INTEGER DEFAULT 1,
            course_done    INTEGER DEFAULT 0,
            registered_at  TEXT DEFAULT (datetime('now')),
            is_active      INTEGER DEFAULT 1,
            approved       INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS homework (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER NOT NULL,
            lesson_num   INTEGER NOT NULL,
            answer       TEXT NOT NULL,
            file_id      TEXT,
            status       TEXT DEFAULT 'pending',
            feedback     TEXT,
            submitted_at TEXT DEFAULT (datetime('now')),
            reviewed_at  TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
    """)
    conn.commit()
    conn.close()


# ── Users ───────────────────────────────────────────────────────

def register_user(user_id: int, username: str, full_name: str) -> bool:
    conn = get_connection()
    existing = conn.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,)).fetchone()
    if existing:
        conn.close()
        return False
    conn.execute(
        "INSERT INTO users (user_id, username, full_name, approved) VALUES (?, ?, ?, 0)",
        (user_id, username, full_name)
    )
    conn.commit()
    conn.close()
    return True


def approve_user(user_id: int):
    conn = get_connection()
    conn.execute("UPDATE users SET approved=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()


def reject_user(user_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM users WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()


def get_user(user_id: int) -> Optional[dict]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_all_active_users() -> list:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM users WHERE is_active=1 AND approved=1").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def advance_lesson(user_id: int):
    conn = get_connection()
    conn.execute(
        "UPDATE users SET current_lesson = current_lesson + 1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()
    conn.close()


def complete_course(user_id: int):
    conn = get_connection()
    conn.execute("UPDATE users SET course_done=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()


def get_stats() -> dict:
    conn = get_connection()
    total = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    active = conn.execute("SELECT COUNT(*) FROM users WHERE is_active=1").fetchone()[0]
    done = conn.execute("SELECT COUNT(*) FROM users WHERE course_done=1").fetchone()[0]
    pending_approval = conn.execute("SELECT COUNT(*) FROM users WHERE approved=0").fetchone()[0]
    hw_pending = conn.execute("SELECT COUNT(*) FROM homework WHERE status='pending'").fetchone()[0]
    hw_approved = conn.execute("SELECT COUNT(*) FROM homework WHERE status='approved'").fetchone()[0]
    conn.close()
    return {
        "total": total, "active": active, "done": done,
        "pending_approval": pending_approval,
        "hw_pending": hw_pending, "hw_approved": hw_approved
    }


def get_pending_users() -> list:
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM users WHERE approved=0 ORDER BY registered_at"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ── Homework ─────────────────────────────────────────────────────

def submit_homework(user_id: int, lesson_num: int, answer: str, file_id: str = None) -> int:
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO homework (user_id, lesson_num, answer, file_id) VALUES (?, ?, ?, ?)",
        (user_id, lesson_num, answer, file_id)
    )
    hw_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return hw_id


def get_pending_homework() -> list:
    conn = get_connection()
    rows = conn.execute("""
        SELECT h.*, u.full_name, u.username
        FROM homework h JOIN users u ON h.user_id = u.user_id
        WHERE h.status = 'pending'
        ORDER BY h.submitted_at
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def review_homework(hw_id: int, status: str, feedback: str = None):
    conn = get_connection()
    conn.execute(
        "UPDATE homework SET status=?, feedback=?, reviewed_at=datetime('now') WHERE id=?",
        (status, feedback, hw_id)
    )
    conn.commit()
    conn.close()


def get_homework_by_id(hw_id: int) -> Optional[dict]:
    conn = get_connection()
    row = conn.execute("SELECT * FROM homework WHERE id=?", (hw_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


init_db()
