session_stats = {'done': 10, 'todo': 0}
if session_stats['todo']:
    print(f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}")
else:
    print(f"Good job! All {session_stats['done']} pomodoros done!")