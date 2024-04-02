## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file trigonometrie023.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_172 = Integer(172); _sage_const_175 = Integer(175); _sage_const_177 = Integer(177); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_194 = Integer(194); _sage_const_197 = Integer(197); _sage_const_199 = Integer(199); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_216 = Integer(216); _sage_const_219 = Integer(219); _sage_const_221 = Integer(221); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_223 = Integer(223); _sage_const_6 = Integer(6); _sage_const_230 = Integer(230); _sage_const_233 = Integer(233); _sage_const_235 = Integer(235); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_262 = Integer(262); _sage_const_265 = Integer(265); _sage_const_267 = Integer(267); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_269 = Integer(269); _sage_const_11 = Integer(11); _sage_const_273 = Integer(273); _sage_const_299 = Integer(299); _sage_const_302 = Integer(302); _sage_const_304 = Integer(304); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_329 = Integer(329); _sage_const_332 = Integer(332); _sage_const_334 = Integer(334); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_337 = Integer(337); _sage_const_16 = Integer(16); _sage_const_341 = Integer(341); _sage_const_371 = Integer(371); _sage_const_374 = Integer(374); _sage_const_376 = Integer(376); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_403 = Integer(403); _sage_const_406 = Integer(406); _sage_const_408 = Integer(408); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_410 = Integer(410); _sage_const_21 = Integer(21); _sage_const_414 = Integer(414); _sage_const_447 = Integer(447); _sage_const_450 = Integer(450); _sage_const_452 = Integer(452); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_498 = Integer(498); _sage_const_501 = Integer(501); _sage_const_504 = Integer(504); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_506 = Integer(506); _sage_const_26 = Integer(26); _sage_const_510 = Integer(510); _sage_const_540 = Integer(540); _sage_const_543 = Integer(543); _sage_const_545 = Integer(545); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_547 = Integer(547); _sage_const_29 = Integer(29); _sage_const_551 = Integer(551); _sage_const_577 = Integer(577); _sage_const_580 = Integer(580); _sage_const_583 = Integer(583); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_585 = Integer(585); _sage_const_32 = Integer(32); _sage_const_589 = Integer(589); _sage_const_620 = Integer(620); _sage_const_623 = Integer(623); _sage_const_626 = Integer(626); _sage_const_33 = Integer(33); _sage_const_34 = Integer(34); _sage_const_630 = Integer(630); _sage_const_35 = Integer(35); _sage_const_634 = Integer(634); _sage_const_667 = Integer(667); _sage_const_670 = Integer(670); _sage_const_673 = Integer(673); _sage_const_36 = Integer(36); _sage_const_37 = Integer(37); _sage_const_677 = Integer(677); _sage_const_38 = Integer(38); _sage_const_681 = Integer(681); _sage_const_755 = Integer(755); _sage_const_758 = Integer(758); _sage_const_760 = Integer(760); _sage_const_39 = Integer(39); _sage_const_40 = Integer(40); _sage_const_762 = Integer(762); _sage_const_41 = Integer(41); _sage_const_766 = Integer(766); _sage_const_800 = Integer(800); _sage_const_803 = Integer(803); _sage_const_805 = Integer(805); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43)## This file (trigonometrie023.sagetex.sage) was *autogenerated* from trigonometrie023.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('trigonometrie023', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_172 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cos(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_175 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_177 
 _st_.inline(_sage_const_0 , latex(f(x)))
except:
 _st_.goboom(_sage_const_177 )
try:
 _st_.current_tex_line = _sage_const_177 
 _st_.inline(_sage_const_1 , latex(F(x)))
except:
 _st_.goboom(_sage_const_177 )
_st_.current_tex_line = _sage_const_194 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sin(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_197 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_199 
 _st_.inline(_sage_const_2 , latex(f(x)))
except:
 _st_.goboom(_sage_const_199 )
try:
 _st_.current_tex_line = _sage_const_199 
 _st_.inline(_sage_const_3 , latex(F(x)))
except:
 _st_.goboom(_sage_const_199 )
_st_.current_tex_line = _sage_const_216 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_219 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_221 
 _st_.inline(_sage_const_4 , latex(f(x)))
except:
 _st_.goboom(_sage_const_221 )
try:
 _st_.current_tex_line = _sage_const_221 
 _st_.inline(_sage_const_5 , latex(g(x)))
except:
 _st_.goboom(_sage_const_221 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_6 , latex(f(x)))
except:
 _st_.goboom(_sage_const_223 )
_st_.current_tex_line = _sage_const_230 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tan(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_233 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_7 , latex(f(x)))
except:
 _st_.goboom(_sage_const_235 )
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_8 , latex(F(x)))
except:
 _st_.goboom(_sage_const_235 )
_st_.current_tex_line = _sage_const_262 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_265 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_267 
 _st_.inline(_sage_const_9 , latex(f(x)))
except:
 _st_.goboom(_sage_const_267 )
try:
 _st_.current_tex_line = _sage_const_267 
 _st_.inline(_sage_const_10 , latex(g(x)))
except:
 _st_.goboom(_sage_const_267 )
try:
 _st_.current_tex_line = _sage_const_269 
 _st_.inline(_sage_const_11 , latex(f(x)))
except:
 _st_.goboom(_sage_const_269 )
try:
 _st_.current_tex_line = _sage_const_273 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_273 )
_st_.current_tex_line = _sage_const_299 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_302 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_304 
 _st_.inline(_sage_const_12 , latex(f(x)))
except:
 _st_.goboom(_sage_const_304 )
try:
 _st_.current_tex_line = _sage_const_304 
 _st_.inline(_sage_const_13 , latex(F(x)))
except:
 _st_.goboom(_sage_const_304 )
_st_.current_tex_line = _sage_const_329 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_332 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_334 
 _st_.inline(_sage_const_14 , latex(f(x)))
except:
 _st_.goboom(_sage_const_334 )
try:
 _st_.current_tex_line = _sage_const_334 
 _st_.inline(_sage_const_15 , latex(g(x)))
except:
 _st_.goboom(_sage_const_334 )
try:
 _st_.current_tex_line = _sage_const_337 
 _st_.inline(_sage_const_16 , latex(f(x)))
except:
 _st_.goboom(_sage_const_337 )
try:
 _st_.current_tex_line = _sage_const_341 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_341 )
_st_.current_tex_line = _sage_const_371 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_374 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_376 
 _st_.inline(_sage_const_17 , latex(f(x)))
except:
 _st_.goboom(_sage_const_376 )
try:
 _st_.current_tex_line = _sage_const_376 
 _st_.inline(_sage_const_18 , latex(F(x)))
except:
 _st_.goboom(_sage_const_376 )
_st_.current_tex_line = _sage_const_403 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_406 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_408 
 _st_.inline(_sage_const_19 , latex(f(x)))
except:
 _st_.goboom(_sage_const_408 )
try:
 _st_.current_tex_line = _sage_const_408 
 _st_.inline(_sage_const_20 , latex(g(x)))
except:
 _st_.goboom(_sage_const_408 )
try:
 _st_.current_tex_line = _sage_const_410 
 _st_.inline(_sage_const_21 , latex(f(x)))
except:
 _st_.goboom(_sage_const_410 )
try:
 _st_.current_tex_line = _sage_const_414 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=plot(f(x), x, -_sage_const_10 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_414 )
_st_.current_tex_line = _sage_const_447 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_450 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_452 
 _st_.inline(_sage_const_22 , latex(f(x)))
except:
 _st_.goboom(_sage_const_452 )
try:
 _st_.current_tex_line = _sage_const_452 
 _st_.inline(_sage_const_23 , latex(F(x)))
except:
 _st_.goboom(_sage_const_452 )
_st_.current_tex_line = _sage_const_498 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sinh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_501 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_504 
 _st_.inline(_sage_const_24 , latex(f(x)))
except:
 _st_.goboom(_sage_const_504 )
try:
 _st_.current_tex_line = _sage_const_504 
 _st_.inline(_sage_const_25 , latex(F(x)))
except:
 _st_.goboom(_sage_const_504 )
try:
 _st_.current_tex_line = _sage_const_506 
 _st_.inline(_sage_const_26 , latex(f(x)))
except:
 _st_.goboom(_sage_const_506 )
try:
 _st_.current_tex_line = _sage_const_510 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=plot(f(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_510 )
_st_.current_tex_line = _sage_const_540 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_543 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_545 
 _st_.inline(_sage_const_27 , latex(f(x)))
except:
 _st_.goboom(_sage_const_545 )
try:
 _st_.current_tex_line = _sage_const_545 
 _st_.inline(_sage_const_28 , latex(F(x)))
except:
 _st_.goboom(_sage_const_545 )
try:
 _st_.current_tex_line = _sage_const_547 
 _st_.inline(_sage_const_29 , latex(f(x)))
except:
 _st_.goboom(_sage_const_547 )
try:
 _st_.current_tex_line = _sage_const_551 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=plot(f(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_551 )
_st_.current_tex_line = _sage_const_577 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(acosh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_580 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_583 
 _st_.inline(_sage_const_30 , latex(f(x)))
except:
 _st_.goboom(_sage_const_583 )
try:
 _st_.current_tex_line = _sage_const_583 
 _st_.inline(_sage_const_31 , latex(F(x)))
except:
 _st_.goboom(_sage_const_583 )
try:
 _st_.current_tex_line = _sage_const_585 
 _st_.inline(_sage_const_32 , latex(f(x)))
except:
 _st_.goboom(_sage_const_585 )
try:
 _st_.current_tex_line = _sage_const_589 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_589 )
_st_.current_tex_line = _sage_const_620 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(asinh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_623 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_626 
 _st_.inline(_sage_const_33 , latex(f(x)))
except:
 _st_.goboom(_sage_const_626 )
try:
 _st_.current_tex_line = _sage_const_626 
 _st_.inline(_sage_const_34 , latex(F(x)))
except:
 _st_.goboom(_sage_const_626 )
try:
 _st_.current_tex_line = _sage_const_630 
 _st_.inline(_sage_const_35 , latex(f(x)))
except:
 _st_.goboom(_sage_const_630 )
try:
 _st_.current_tex_line = _sage_const_634 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=plot(f(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_634 )
_st_.current_tex_line = _sage_const_667 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(atanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_670 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_673 
 _st_.inline(_sage_const_36 , latex(f(x)))
except:
 _st_.goboom(_sage_const_673 )
try:
 _st_.current_tex_line = _sage_const_673 
 _st_.inline(_sage_const_37 , latex(F(x)))
except:
 _st_.goboom(_sage_const_673 )
try:
 _st_.current_tex_line = _sage_const_677 
 _st_.inline(_sage_const_38 , latex(f(x)))
except:
 _st_.goboom(_sage_const_677 )
try:
 _st_.current_tex_line = _sage_const_681 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_681 )
_st_.current_tex_line = _sage_const_755 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(ln(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_758 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_760 
 _st_.inline(_sage_const_39 , latex(f(x)))
except:
 _st_.goboom(_sage_const_760 )
try:
 _st_.current_tex_line = _sage_const_760 
 _st_.inline(_sage_const_40 , latex(g(x)))
except:
 _st_.goboom(_sage_const_760 )
try:
 _st_.current_tex_line = _sage_const_762 
 _st_.inline(_sage_const_41 , latex(f(x)))
except:
 _st_.goboom(_sage_const_762 )
try:
 _st_.current_tex_line = _sage_const_766 
 _st_.plot(_sage_const_8 , format='notprovided', _p_=plot(f(x), x, _sage_const_0 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_766 )
_st_.current_tex_line = _sage_const_800 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(log(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_803 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_805 
 _st_.inline(_sage_const_42 , latex(f(x)))
except:
 _st_.goboom(_sage_const_805 )
try:
 _st_.current_tex_line = _sage_const_805 
 _st_.inline(_sage_const_43 , latex(F(x)))
except:
 _st_.goboom(_sage_const_805 )
_st_.endofdoc()

