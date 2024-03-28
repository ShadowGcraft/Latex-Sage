## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file trigonometrie023.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_174 = Integer(174); _sage_const_177 = Integer(177); _sage_const_179 = Integer(179); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_197 = Integer(197); _sage_const_200 = Integer(200); _sage_const_202 = Integer(202); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_218 = Integer(218); _sage_const_221 = Integer(221); _sage_const_223 = Integer(223); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_225 = Integer(225); _sage_const_6 = Integer(6); _sage_const_235 = Integer(235); _sage_const_238 = Integer(238); _sage_const_240 = Integer(240); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_265 = Integer(265); _sage_const_268 = Integer(268); _sage_const_270 = Integer(270); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_272 = Integer(272); _sage_const_11 = Integer(11); _sage_const_276 = Integer(276); _sage_const_302 = Integer(302); _sage_const_305 = Integer(305); _sage_const_307 = Integer(307); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_332 = Integer(332); _sage_const_335 = Integer(335); _sage_const_337 = Integer(337); _sage_const_14 = Integer(14); _sage_const_15 = Integer(15); _sage_const_340 = Integer(340); _sage_const_16 = Integer(16); _sage_const_344 = Integer(344); _sage_const_374 = Integer(374); _sage_const_377 = Integer(377); _sage_const_379 = Integer(379); _sage_const_17 = Integer(17); _sage_const_18 = Integer(18); _sage_const_406 = Integer(406); _sage_const_409 = Integer(409); _sage_const_411 = Integer(411); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_413 = Integer(413); _sage_const_21 = Integer(21); _sage_const_417 = Integer(417); _sage_const_450 = Integer(450); _sage_const_453 = Integer(453); _sage_const_455 = Integer(455); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_501 = Integer(501); _sage_const_504 = Integer(504); _sage_const_507 = Integer(507); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_509 = Integer(509); _sage_const_26 = Integer(26); _sage_const_513 = Integer(513); _sage_const_543 = Integer(543); _sage_const_546 = Integer(546); _sage_const_548 = Integer(548); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_572 = Integer(572); _sage_const_575 = Integer(575); _sage_const_578 = Integer(578); _sage_const_29 = Integer(29); _sage_const_30 = Integer(30); _sage_const_580 = Integer(580); _sage_const_31 = Integer(31); _sage_const_584 = Integer(584); _sage_const_615 = Integer(615); _sage_const_618 = Integer(618); _sage_const_621 = Integer(621); _sage_const_32 = Integer(32); _sage_const_33 = Integer(33); _sage_const_625 = Integer(625); _sage_const_34 = Integer(34); _sage_const_629 = Integer(629); _sage_const_662 = Integer(662); _sage_const_665 = Integer(665); _sage_const_668 = Integer(668); _sage_const_35 = Integer(35); _sage_const_36 = Integer(36); _sage_const_672 = Integer(672); _sage_const_37 = Integer(37); _sage_const_676 = Integer(676); _sage_const_750 = Integer(750); _sage_const_753 = Integer(753); _sage_const_755 = Integer(755); _sage_const_38 = Integer(38); _sage_const_39 = Integer(39); _sage_const_757 = Integer(757); _sage_const_40 = Integer(40); _sage_const_761 = Integer(761); _sage_const_795 = Integer(795); _sage_const_798 = Integer(798); _sage_const_800 = Integer(800); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42)## This file (trigonometrie023.sagetex.sage) was *autogenerated* from trigonometrie023.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('trigonometrie023', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_174 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cos(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_177 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_0 , latex(f(x)))
except:
 _st_.goboom(_sage_const_179 )
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_1 , latex(F(x)))
except:
 _st_.goboom(_sage_const_179 )
_st_.current_tex_line = _sage_const_197 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sin(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_200 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_202 
 _st_.inline(_sage_const_2 , latex(f(x)))
except:
 _st_.goboom(_sage_const_202 )
try:
 _st_.current_tex_line = _sage_const_202 
 _st_.inline(_sage_const_3 , latex(F(x)))
except:
 _st_.goboom(_sage_const_202 )
_st_.current_tex_line = _sage_const_218 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_221 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_4 , latex(f(x)))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_5 , latex(g(x)))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_225 
 _st_.inline(_sage_const_6 , latex(f(x)))
except:
 _st_.goboom(_sage_const_225 )
_st_.current_tex_line = _sage_const_235 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tan(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_238 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_240 
 _st_.inline(_sage_const_7 , latex(f(x)))
except:
 _st_.goboom(_sage_const_240 )
try:
 _st_.current_tex_line = _sage_const_240 
 _st_.inline(_sage_const_8 , latex(F(x)))
except:
 _st_.goboom(_sage_const_240 )
_st_.current_tex_line = _sage_const_265 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_268 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_270 
 _st_.inline(_sage_const_9 , latex(f(x)))
except:
 _st_.goboom(_sage_const_270 )
try:
 _st_.current_tex_line = _sage_const_270 
 _st_.inline(_sage_const_10 , latex(g(x)))
except:
 _st_.goboom(_sage_const_270 )
try:
 _st_.current_tex_line = _sage_const_272 
 _st_.inline(_sage_const_11 , latex(f(x)))
except:
 _st_.goboom(_sage_const_272 )
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_276 )
_st_.current_tex_line = _sage_const_302 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_305 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_307 
 _st_.inline(_sage_const_12 , latex(f(x)))
except:
 _st_.goboom(_sage_const_307 )
try:
 _st_.current_tex_line = _sage_const_307 
 _st_.inline(_sage_const_13 , latex(F(x)))
except:
 _st_.goboom(_sage_const_307 )
_st_.current_tex_line = _sage_const_332 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_335 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_337 
 _st_.inline(_sage_const_14 , latex(f(x)))
except:
 _st_.goboom(_sage_const_337 )
try:
 _st_.current_tex_line = _sage_const_337 
 _st_.inline(_sage_const_15 , latex(g(x)))
except:
 _st_.goboom(_sage_const_337 )
try:
 _st_.current_tex_line = _sage_const_340 
 _st_.inline(_sage_const_16 , latex(f(x)))
except:
 _st_.goboom(_sage_const_340 )
try:
 _st_.current_tex_line = _sage_const_344 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_344 )
_st_.current_tex_line = _sage_const_374 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_377 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_379 
 _st_.inline(_sage_const_17 , latex(f(x)))
except:
 _st_.goboom(_sage_const_379 )
try:
 _st_.current_tex_line = _sage_const_379 
 _st_.inline(_sage_const_18 , latex(F(x)))
except:
 _st_.goboom(_sage_const_379 )
_st_.current_tex_line = _sage_const_406 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_409 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_411 
 _st_.inline(_sage_const_19 , latex(f(x)))
except:
 _st_.goboom(_sage_const_411 )
try:
 _st_.current_tex_line = _sage_const_411 
 _st_.inline(_sage_const_20 , latex(g(x)))
except:
 _st_.goboom(_sage_const_411 )
try:
 _st_.current_tex_line = _sage_const_413 
 _st_.inline(_sage_const_21 , latex(f(x)))
except:
 _st_.goboom(_sage_const_413 )
try:
 _st_.current_tex_line = _sage_const_417 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=plot(f(x), x, -_sage_const_10 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_417 )
_st_.current_tex_line = _sage_const_450 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_453 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_455 
 _st_.inline(_sage_const_22 , latex(f(x)))
except:
 _st_.goboom(_sage_const_455 )
try:
 _st_.current_tex_line = _sage_const_455 
 _st_.inline(_sage_const_23 , latex(F(x)))
except:
 _st_.goboom(_sage_const_455 )
_st_.current_tex_line = _sage_const_501 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sinh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_504 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_507 
 _st_.inline(_sage_const_24 , latex(f(x)))
except:
 _st_.goboom(_sage_const_507 )
try:
 _st_.current_tex_line = _sage_const_507 
 _st_.inline(_sage_const_25 , latex(F(x)))
except:
 _st_.goboom(_sage_const_507 )
try:
 _st_.current_tex_line = _sage_const_509 
 _st_.inline(_sage_const_26 , latex(f(x)))
except:
 _st_.goboom(_sage_const_509 )
try:
 _st_.current_tex_line = _sage_const_513 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=plot(f(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_513 )
_st_.current_tex_line = _sage_const_543 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_546 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_548 
 _st_.inline(_sage_const_27 , latex(f(x)))
except:
 _st_.goboom(_sage_const_548 )
try:
 _st_.current_tex_line = _sage_const_548 
 _st_.inline(_sage_const_28 , latex(F(x)))
except:
 _st_.goboom(_sage_const_548 )
_st_.current_tex_line = _sage_const_572 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(acosh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_575 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_578 
 _st_.inline(_sage_const_29 , latex(f(x)))
except:
 _st_.goboom(_sage_const_578 )
try:
 _st_.current_tex_line = _sage_const_578 
 _st_.inline(_sage_const_30 , latex(F(x)))
except:
 _st_.goboom(_sage_const_578 )
try:
 _st_.current_tex_line = _sage_const_580 
 _st_.inline(_sage_const_31 , latex(f(x)))
except:
 _st_.goboom(_sage_const_580 )
try:
 _st_.current_tex_line = _sage_const_584 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 ,_sage_const_5 ))
except:
 _st_.goboom(_sage_const_584 )
_st_.current_tex_line = _sage_const_615 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(asinh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_618 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_621 
 _st_.inline(_sage_const_32 , latex(f(x)))
except:
 _st_.goboom(_sage_const_621 )
try:
 _st_.current_tex_line = _sage_const_621 
 _st_.inline(_sage_const_33 , latex(F(x)))
except:
 _st_.goboom(_sage_const_621 )
try:
 _st_.current_tex_line = _sage_const_625 
 _st_.inline(_sage_const_34 , latex(f(x)))
except:
 _st_.goboom(_sage_const_625 )
try:
 _st_.current_tex_line = _sage_const_629 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=plot(f(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_629 )
_st_.current_tex_line = _sage_const_662 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(atanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_665 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_668 
 _st_.inline(_sage_const_35 , latex(f(x)))
except:
 _st_.goboom(_sage_const_668 )
try:
 _st_.current_tex_line = _sage_const_668 
 _st_.inline(_sage_const_36 , latex(F(x)))
except:
 _st_.goboom(_sage_const_668 )
try:
 _st_.current_tex_line = _sage_const_672 
 _st_.inline(_sage_const_37 , latex(f(x)))
except:
 _st_.goboom(_sage_const_672 )
try:
 _st_.current_tex_line = _sage_const_676 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_676 )
_st_.current_tex_line = _sage_const_750 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(ln(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_753 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_755 
 _st_.inline(_sage_const_38 , latex(f(x)))
except:
 _st_.goboom(_sage_const_755 )
try:
 _st_.current_tex_line = _sage_const_755 
 _st_.inline(_sage_const_39 , latex(g(x)))
except:
 _st_.goboom(_sage_const_755 )
try:
 _st_.current_tex_line = _sage_const_757 
 _st_.inline(_sage_const_40 , latex(f(x)))
except:
 _st_.goboom(_sage_const_757 )
try:
 _st_.current_tex_line = _sage_const_761 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(f(x), x, _sage_const_0 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_761 )
_st_.current_tex_line = _sage_const_795 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(log(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_798 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_800 
 _st_.inline(_sage_const_41 , latex(f(x)))
except:
 _st_.goboom(_sage_const_800 )
try:
 _st_.current_tex_line = _sage_const_800 
 _st_.inline(_sage_const_42 , latex(F(x)))
except:
 _st_.goboom(_sage_const_800 )
_st_.endofdoc()

