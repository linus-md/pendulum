print("This is not a single pendulum, but a double pendulum!!!!");
vars := [x1, y1, u1, v1, x2, y2, u2, v2];
p := [
    u1, 
    v1, 
    - x1 - (x1 - x2), 
    - y1 - (y1 - y2) - 1, 
    u2, 
    v2, 
    x2 - x1, 
    y2 - y1 - 1
    ];
q := [x1^2 + y1^2 - 1, (x2 - x1)^2 + (y2 - y1)^2 - 1];
