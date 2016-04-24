// Benchmark "c8" written by ABC on Wed Apr 13 22:18:47 2016

module c8 ( 
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, u, v, w, x, y,
    z, a0, b0, c0,
    d0, e0, f0, g0, h0, i0, j0, k0, l0, m0, n0, o0, p0, q0, r0, s0, t0, u0  );
  input  a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, u, v,
    w, x, y, z, a0, b0, c0;
  output d0, e0, f0, g0, h0, i0, j0, k0, l0, m0, n0, o0, p0, q0, r0, s0, t0,
    u0;
  wire u1, v1, w1, y1, z1, a2, c2, d2, e2, g2, h2, i2, j2, k2, m2, n2, o2,
    p2, q2, s2, t2, u2, v2, w2, y2, z2, a3, b3, c3, d3;
  assign d0 = (~i & (~u | c0)) | (~u & ~c0);
  assign e0 = (~j & (~v | c0)) | (~v & ~c0);
  assign f0 = (~k & (~w | c0)) | (~w & ~c0);
  assign g0 = (~l & (~x | c0)) | (~x & ~c0);
  assign h0 = (~m & (~y | c0)) | (~y & ~c0);
  assign i0 = (~n & (~z | c0)) | (~z & ~c0);
  assign j0 = (~o & (~a0 | c0)) | (~a0 & ~c0);
  assign k0 = (~p & (~b0 | c0)) | (~b0 & ~c0);
  assign m0 = ((~r ^ u) & ((i & (~s | a)) | q | (s & a))) | (~q & ((i & (~s | a)) | (s & a)));
  assign n0 = ~v1 & (v | ~q | ~u1);
  assign o0 = ~z1 & (~q | ((w | ~y1) & (u | r | ~w1)));
  assign p0 = ~d2 & (~q | ((x | ~c2) & (u | r | ~a2)));
  assign q0 = ~h2 & (~q | ((y | ~g2) & (u | r | ~e2)));
  assign r0 = ~n2 & (~q | ((z | ~m2) & (r | ~j2 | ~k2)));
  assign s0 = ~t2 & (~q | ((a0 | ~s2) & (r | ~p2 | ~q2)));
  assign t0 = ~z2 & (~q | ((b0 | ~y2) & (r | ~v2 | ~w2)));
  assign u0 = q & (r ? c0 : (~c3 & ~d3));
  assign u1 = u | r;
  assign v1 = (~q & (s ? ~b : ~j)) | (q & ~r & ~u & v);
  assign w1 = w & ~v;
  assign y1 = r | v | u;
  assign z1 = ~q & ((~c & (~k | s)) | (~k & ~s));
  assign a2 = ~v & x & ~w;
  assign c2 = u | r | w | v;
  assign d2 = ~q & ((~d & (~l | s)) | (~l & ~s));
  assign e2 = ~v & ~w & y & ~x;
  assign g2 = r | ~i2 | v | u;
  assign h2 = ~q & ((~e & (~m | s)) | (~m & ~s));
  assign i2 = ~x & ~w;
  assign j2 = ~v & ~u;
  assign k2 = ~w & ~x & z & ~y;
  assign m2 = r | ~o2 | v | u;
  assign n2 = ~q & ((~f & (~n | s)) | (~n & ~s));
  assign o2 = ~w & ~y & ~x;
  assign p2 = ~u & ~w & ~v;
  assign q2 = ~x & ~y & a0 & ~z;
  assign s2 = r | ~u2 | v | u;
  assign t2 = ~q & ((~g & (~o | s)) | (~o & ~s));
  assign u2 = ~w & ~x & ~z & ~y;
  assign v2 = ~u & ~v & ~x & ~w;
  assign w2 = ~y & ~z & b0 & ~a0;
  assign y2 = ~a3 | ~b3 | u | r;
  assign z2 = ~q & ((~h & (~p | s)) | (~p & ~s));
  assign a3 = ~w & ~v;
  assign b3 = ~x & ~y & ~a0 & ~z;
  assign c3 = v | ~u | x | w;
  assign d3 = z | y | b0 | a0;
  assign l0 = c0;
endmodule


