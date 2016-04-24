// Benchmark "mux" written by ABC on Wed Apr 13 22:17:38 2016

module mux ( 
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u,
    v  );
  input  a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u;
  output v;
  wire b0, e0, f0, g0, j0;
  assign v = u & j0;
  assign b0 = (~m & ((~n & (s | (~o & ~p))) | (t & (~o | s)))) | (~t & ((~n & (~p | s)) | (~p & ~s))) | (~o & ~s & (~p | t));
  assign e0 = (~i & ((~j & (s | (~k & ~l))) | (t & (~k | s)))) | (~t & ((~j & (~l | s)) | (~l & ~s))) | (~k & ~s & (~l | t));
  assign f0 = (~e & ((~f & (s | (~g & ~h))) | (t & (~g | s)))) | (~t & ((~f & (~h | s)) | (~h & ~s))) | (~g & ~s & (~h | t));
  assign g0 = (~a & ((~b & (s | (~c & ~d))) | (t & (~c | s)))) | (~t & ((~b & (~d | s)) | (~d & ~s))) | (~c & ~s & (~d | t));
  assign j0 = (~f0 & ((q & (~r | ~g0)) | (~b0 & (~r | (~e0 & ~g0))))) | (~q & ((~b0 & (~r | ~e0)) | (r & ~e0))) | (r & ~g0 & (q | ~e0));
endmodule


