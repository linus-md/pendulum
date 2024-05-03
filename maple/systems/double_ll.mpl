vars := [x1, y1, u1, v1, x2, y2, u2, v2, l1, l2];

p := [
    u1,
    v1,
    - l1*x1 - l2*(x1 - x2),
    - l1*y1 - l2*(y1 - y2) - 1,
    u2,
    v2,
    - l2*(x2 - x1),
    - l2*(y2 - y1) - 1,
    0,
    0];

q := [x1^2 + y1^2 - 1, (x2 - x1)^2 + (y2 - y1)^2 - 1];