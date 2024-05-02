with(Groebner);
infolevel[GroebnerBasis] := 5;
partial := proc(q, p, vars) 
	local i; 
	return add(p[i]*diff(q, vars[i]), i = 1 .. nops(vars)); 
end proc;

algorithm := proc(qs, p, vars) 
	local S, G, gs, i, tord; 
	i := 0; 
	tord := tdeg(op(vars)); 
	gs := qs; 
    print(gs);
	G := Basis(qs, tord); 
	while true do
		i := i + 1;
		gs := map(g ->  NormalForm(partial(g, p, vars), G, tord), gs);
		gs := remove(`=`, gs, 0);
		if nops(gs) = 0 then
			return G;
		fi;
		G := [op(G), op(gs)]; 
		G := Basis(G, tord); 
		end do; 
	return G; 
end proc;

# Simple double pendulum
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

#algorithm(q, p, vars);


# Not really a Chemical reaction network (66s)
vars1 := [x1, x2, x3, x4, x5, x6, k1, k2, k3, k4, k5, k6];
p1 := [
    - k1*x1 + k4*x3*x5, 
    k1*x1 - k2*x2 + k5*x4*x5, 
    - k3*x3 + k2*x2 + k4*x3*x5, 
    k3*x3 - k5*x4*x5,
    - k4*x3*x5 - k5*x4*x5 + k6*x6, 
    k4*x3*x5 - k6*x6 + k5*x4*x5,
    0, 0, 0, 0, 0, 0
    ];
q1 := [x1 + x2 + x3 + x4 - 1, x5 + x6 - 1];

algorithm(q1, p1, vars1);