CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    done BOOLEAN DEFAULT 0
);

INSERT INTO tasks (id, name, done) VALUES (1, 'Learn Docker', 0);
INSERT INTO tasks (id, name, done) VALUES (2, 'Deploy to AWS', 1);

SELECT * FROM tasks WHERE done = 0;
UPDATE tasks SET done = 1 WHERE id = 1;
SELECT COUNT(*) AS completed_tasks FROM tasks WHERE done = 1;