import sqlite3
DB_NAME = 'tasks.db'

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    #テーブル作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        discordID string,
        taskID INTEGER PRIMARY KEY,
        time TEXT NOT NULL,
        title TEXT NOT NULL,
        details TEXT,
        notified INTEGER DEFAULT 0
    )
    ''')
    
    conn.commit()
    conn.close()
    
    print(f"データベース'{DB_NAME}'が作成されました")

#タスク追加の関数
def add_Task(discordID,taskID,time,title,details):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
    
        INSERT INTO tasks (discordID,time,title,details)
        VALUES (?,?,?,?)
    ''',(discordID,time,title,details))
    
    taskID = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return taskID   

#タスク一覧を見る関数
def view_Task(discordID):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
                   
        SELECT taskID,time,title,details
        FROM tasks
        WHERE discordID = ?
        ORDER BY time
        
    ''',(discordID))
    
    tasks = cursor.fetchall()
    
    conn.close()
    
    return tasks

#IDを指定してタスクの中身を変更する関数
def update_Task(TaskID,time = None,title = None,details = None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    #現在のタスクを取得
    cursor.execute('SELECT time,title,details FROM tasks WHERE taskID = ?',(TaskID))
    current_task = cursor.fetchone()
    
    if current_task:
        new_time = time if time is not None else current_task[0]
        new_title = title if title is not None else current_task[1]
        new_details = details if details is not None else current_task[2]
        
        cursor.execute('''(
        UPDATE tasks
        time = ? ,title = ?, details = ?
        WHERE TaskID = ?
        )''',(new_time,new_title,new_details,TaskID))
    
        return True
    else:
        return False

#ID指定でタスクの削除
def delete_Task(taskID):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM tasks WHERE taskID = ?', (taskID,))
    
    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
# データベースの初期化
create_database()

        