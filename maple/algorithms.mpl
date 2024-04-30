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
	G := Basis(qs, tord); 
	while true do
		i := i + 1; 
		print(cat("Iteration ", i, " g= ", g)); 
		gs := map(g ->  NormalForm(partial(g, p, vars), G, tord), gs);
		gs := remove(`=`, gs, 0);
		if nops(gs) = 0 then
			return G;
		fi;
		G := [op(G), op(gs)]; 
		G := Basis(G, tord); 
		print(G); end 	do; 
	return G; 
end proc;