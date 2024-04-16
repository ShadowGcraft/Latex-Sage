## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file trigonometrie05.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_206 = Integer(206); _sage_const_210 = Integer(210); _sage_const_212 = Integer(212); _sage_const_0 = Integer(0); _sage_const_229 = Integer(229); _sage_const_1 = Integer(1); _sage_const_234 = Integer(234); _sage_const_238 = Integer(238); _sage_const_242 = Integer(242); _sage_const_259 = Integer(259); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_264 = Integer(264); _sage_const_268 = Integer(268); _sage_const_271 = Integer(271); _sage_const_1p4 = RealNumber('1.4'); _sage_const_286 = Integer(286); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_297 = Integer(297); _sage_const_6 = Integer(6); _sage_const_7 = Integer(7); _sage_const_306 = Integer(306); _sage_const_310 = Integer(310); _sage_const_321 = Integer(321); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_325 = Integer(325); _sage_const_326 = Integer(326); _sage_const_327 = Integer(327); _sage_const_10 = Integer(10); _sage_const_340 = Integer(340); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_348 = Integer(348); _sage_const_352 = Integer(352); _sage_const_363 = Integer(363); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_367 = Integer(367); _sage_const_368 = Integer(368); _sage_const_369 = Integer(369); _sage_const_15 = Integer(15); _sage_const_383 = Integer(383); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_392 = Integer(392); _sage_const_396 = Integer(396); _sage_const_403 = Integer(403); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_406 = Integer(406); _sage_const_407 = Integer(407); _sage_const_408 = Integer(408); _sage_const_20 = Integer(20); _sage_const_423 = Integer(423); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_440 = Integer(440); _sage_const_444 = Integer(444); _sage_const_449 = Integer(449); _sage_const_450 = Integer(450); _sage_const_451 = Integer(451); _sage_const_23 = Integer(23); _sage_const_465 = Integer(465); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_474 = Integer(474); _sage_const_478 = Integer(478); _sage_const_481 = Integer(481); _sage_const_482 = Integer(482); _sage_const_483 = Integer(483); _sage_const_26 = Integer(26); _sage_const_499 = Integer(499); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_506 = Integer(506); _sage_const_510 = Integer(510); _sage_const_514 = Integer(514); _sage_const_515 = Integer(515); _sage_const_516 = Integer(516); _sage_const_29 = Integer(29); _sage_const_537 = Integer(537); _sage_const_538 = Integer(538); _sage_const_30 = Integer(30); _sage_const_554 = Integer(554); _sage_const_557 = Integer(557); _sage_const_559 = Integer(559); _sage_const_31 = Integer(31); _sage_const_32 = Integer(32); _sage_const_576 = Integer(576); _sage_const_598 = Integer(598); _sage_const_602 = Integer(602); _sage_const_604 = Integer(604); _sage_const_33 = Integer(33); _sage_const_34 = Integer(34); _sage_const_620 = Integer(620); _sage_const_35 = Integer(35); _sage_const_36 = Integer(36); _sage_const_623 = Integer(623); _sage_const_624 = Integer(624); _sage_const_625 = Integer(625); _sage_const_638 = Integer(638); _sage_const_659 = Integer(659); _sage_const_663 = Integer(663); _sage_const_665 = Integer(665); _sage_const_37 = Integer(37); _sage_const_38 = Integer(38); _sage_const_682 = Integer(682); _sage_const_39 = Integer(39); _sage_const_40 = Integer(40); _sage_const_685 = Integer(685); _sage_const_686 = Integer(686); _sage_const_687 = Integer(687); _sage_const_698 = Integer(698); _sage_const_721 = Integer(721); _sage_const_725 = Integer(725); _sage_const_727 = Integer(727); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_743 = Integer(743); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_746 = Integer(746); _sage_const_747 = Integer(747); _sage_const_0p9 = RealNumber('0.9'); _sage_const_748 = Integer(748); _sage_const_840 = Integer(840); _sage_const_843 = Integer(843); _sage_const_845 = Integer(845); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_847 = Integer(847); _sage_const_47 = Integer(47); _sage_const_851 = Integer(851); _sage_const_877 = Integer(877); _sage_const_880 = Integer(880); _sage_const_882 = Integer(882); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_902 = Integer(902); _sage_const_903 = Integer(903); _sage_const_909 = Integer(909); _sage_const_910 = Integer(910); _sage_const_953 = Integer(953); _sage_const_955 = Integer(955); _sage_const_958 = Integer(958); _sage_const_959 = Integer(959); _sage_const_960 = Integer(960); _sage_const_978 = Integer(978); _sage_const_979 = Integer(979); _sage_const_1012 = Integer(1012); _sage_const_1014 = Integer(1014)## This file (trigonometrie05.sagetex.sage) was *autogenerated* from trigonometrie05.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('trigonometrie05', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_206 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_210 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_212 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=plot(cos(x), x, -pi, pi))
except:
 _st_.goboom(_sage_const_212 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_0 , latex(f(x)))
except:
 _st_.goboom(_sage_const_229 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_1 , latex(F(x)))
except:
 _st_.goboom(_sage_const_229 )
_st_.current_tex_line = _sage_const_234 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_238 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_242 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=plot(sin(x), x, -pi, pi))
except:
 _st_.goboom(_sage_const_242 )
try:
 _st_.current_tex_line = _sage_const_259 
 _st_.inline(_sage_const_2 , latex(f(x)))
except:
 _st_.goboom(_sage_const_259 )
try:
 _st_.current_tex_line = _sage_const_259 
 _st_.inline(_sage_const_3 , latex(F(x)))
except:
 _st_.goboom(_sage_const_259 )
_st_.current_tex_line = _sage_const_264 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_268 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_271 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=plot(tan(x), x, -_sage_const_1p4 , _sage_const_1p4 ))
except:
 _st_.goboom(_sage_const_271 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.inline(_sage_const_4 , latex(f(x)))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.inline(_sage_const_5 , latex(g(x)))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_297 
 _st_.inline(_sage_const_6 , latex(f(x)))
except:
 _st_.goboom(_sage_const_297 )
try:
 _st_.current_tex_line = _sage_const_297 
 _st_.inline(_sage_const_7 , latex(F(x)))
except:
 _st_.goboom(_sage_const_297 )
_st_.current_tex_line = _sage_const_306 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_310 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_321 
 _st_.inline(_sage_const_8 , latex(f(x)))
except:
 _st_.goboom(_sage_const_321 )
try:
 _st_.current_tex_line = _sage_const_321 
 _st_.inline(_sage_const_9 , latex(g(x)))
except:
 _st_.goboom(_sage_const_321 )
try:
 _st_.current_tex_line = _sage_const_325 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_325 )
try:
 _st_.current_tex_line = _sage_const_326 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=plot(cos(x), x, _sage_const_0 , pi))
except:
 _st_.goboom(_sage_const_326 )
try:
 _st_.current_tex_line = _sage_const_327 
 _st_.inline(_sage_const_10 , latex(f(x)))
except:
 _st_.goboom(_sage_const_327 )
try:
 _st_.current_tex_line = _sage_const_340 
 _st_.inline(_sage_const_11 , latex(f(x)))
except:
 _st_.goboom(_sage_const_340 )
try:
 _st_.current_tex_line = _sage_const_340 
 _st_.inline(_sage_const_12 , latex(F(x)))
except:
 _st_.goboom(_sage_const_340 )
_st_.current_tex_line = _sage_const_348 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_352 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_363 
 _st_.inline(_sage_const_13 , latex(f(x)))
except:
 _st_.goboom(_sage_const_363 )
try:
 _st_.current_tex_line = _sage_const_363 
 _st_.inline(_sage_const_14 , latex(g(x)))
except:
 _st_.goboom(_sage_const_363 )
try:
 _st_.current_tex_line = _sage_const_367 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_367 )
try:
 _st_.current_tex_line = _sage_const_368 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=plot(sin(x), x, -pi/_sage_const_2 , pi/_sage_const_2 ))
except:
 _st_.goboom(_sage_const_368 )
try:
 _st_.current_tex_line = _sage_const_369 
 _st_.inline(_sage_const_15 , latex(f(x)))
except:
 _st_.goboom(_sage_const_369 )
try:
 _st_.current_tex_line = _sage_const_383 
 _st_.inline(_sage_const_16 , latex(f(x)))
except:
 _st_.goboom(_sage_const_383 )
try:
 _st_.current_tex_line = _sage_const_383 
 _st_.inline(_sage_const_17 , latex(F(x)))
except:
 _st_.goboom(_sage_const_383 )
_st_.current_tex_line = _sage_const_392 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_396 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_403 
 _st_.inline(_sage_const_18 , latex(f(x)))
except:
 _st_.goboom(_sage_const_403 )
try:
 _st_.current_tex_line = _sage_const_403 
 _st_.inline(_sage_const_19 , latex(g(x)))
except:
 _st_.goboom(_sage_const_403 )
try:
 _st_.current_tex_line = _sage_const_406 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(f(x), x, -_sage_const_10 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_406 )
try:
 _st_.current_tex_line = _sage_const_407 
 _st_.plot(_sage_const_8 , format='notprovided', _p_=plot(tan(x), x, -_sage_const_1p4 , _sage_const_1p4 ))
except:
 _st_.goboom(_sage_const_407 )
try:
 _st_.current_tex_line = _sage_const_408 
 _st_.inline(_sage_const_20 , latex(f(x)))
except:
 _st_.goboom(_sage_const_408 )
try:
 _st_.current_tex_line = _sage_const_423 
 _st_.inline(_sage_const_21 , latex(f(x)))
except:
 _st_.goboom(_sage_const_423 )
try:
 _st_.current_tex_line = _sage_const_423 
 _st_.inline(_sage_const_22 , latex(F(x)))
except:
 _st_.goboom(_sage_const_423 )
_st_.current_tex_line = _sage_const_440 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cosh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_444 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_449 
 _st_.plot(_sage_const_9 , format='notprovided', _p_=plot(f(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_449 )
try:
 _st_.current_tex_line = _sage_const_450 
 _st_.plot(_sage_const_10 , format='notprovided', _p_=plot(g(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_450 )
try:
 _st_.current_tex_line = _sage_const_451 
 _st_.inline(_sage_const_23 , latex(f(x)))
except:
 _st_.goboom(_sage_const_451 )
try:
 _st_.current_tex_line = _sage_const_465 
 _st_.inline(_sage_const_24 , latex(f(x)))
except:
 _st_.goboom(_sage_const_465 )
try:
 _st_.current_tex_line = _sage_const_465 
 _st_.inline(_sage_const_25 , latex(F(x)))
except:
 _st_.goboom(_sage_const_465 )
_st_.current_tex_line = _sage_const_474 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sinh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_478 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_481 
 _st_.plot(_sage_const_11 , format='notprovided', _p_=plot(f(x), x, -_sage_const_3 , _sage_const_3 ))
except:
 _st_.goboom(_sage_const_481 )
try:
 _st_.current_tex_line = _sage_const_482 
 _st_.plot(_sage_const_12 , format='notprovided', _p_=plot(g(x), x, -_sage_const_3 , _sage_const_3 ))
except:
 _st_.goboom(_sage_const_482 )
try:
 _st_.current_tex_line = _sage_const_483 
 _st_.inline(_sage_const_26 , latex(sinh(x)))
except:
 _st_.goboom(_sage_const_483 )
try:
 _st_.current_tex_line = _sage_const_499 
 _st_.inline(_sage_const_27 , latex(f(x)))
except:
 _st_.goboom(_sage_const_499 )
try:
 _st_.current_tex_line = _sage_const_499 
 _st_.inline(_sage_const_28 , latex(F(x)))
except:
 _st_.goboom(_sage_const_499 )
_st_.current_tex_line = _sage_const_506 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tanh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_510 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_514 
 _st_.plot(_sage_const_13 , format='notprovided', _p_=plot(tanh(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_514 )
try:
 _st_.current_tex_line = _sage_const_515 
 _st_.plot(_sage_const_14 , format='notprovided', _p_=plot(diff(tanh(x), x) , x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_515 )
try:
 _st_.current_tex_line = _sage_const_516 
 _st_.inline(_sage_const_29 , latex(tanh(x)))
except:
 _st_.goboom(_sage_const_516 )
try:
 _st_.current_tex_line = _sage_const_537 
 _st_.plot(_sage_const_15 , format='notprovided', _p_=plot(integrate(tanh(x), x) , x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_537 )
try:
 _st_.current_tex_line = _sage_const_538 
 _st_.inline(_sage_const_30 , latex(tanh(x)))
except:
 _st_.goboom(_sage_const_538 )
_st_.current_tex_line = _sage_const_554 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_557 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_559 
 _st_.inline(_sage_const_31 , latex(f(x)))
except:
 _st_.goboom(_sage_const_559 )
try:
 _st_.current_tex_line = _sage_const_559 
 _st_.inline(_sage_const_32 , latex(F(x)))
except:
 _st_.goboom(_sage_const_559 )
try:
 _st_.current_tex_line = _sage_const_576 
 _st_.plot(_sage_const_16 , format='notprovided', _p_=plot(arccosh(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_576 )
_st_.current_tex_line = _sage_const_598 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccosh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_602 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_604 
 _st_.inline(_sage_const_33 , latex(f(x)))
except:
 _st_.goboom(_sage_const_604 )
try:
 _st_.current_tex_line = _sage_const_604 
 _st_.inline(_sage_const_34 , latex(g(x)))
except:
 _st_.goboom(_sage_const_604 )
try:
 _st_.current_tex_line = _sage_const_620 
 _st_.inline(_sage_const_35 , latex(f(x)))
except:
 _st_.goboom(_sage_const_620 )
try:
 _st_.current_tex_line = _sage_const_620 
 _st_.inline(_sage_const_36 , latex(F(x)))
except:
 _st_.goboom(_sage_const_620 )
try:
 _st_.current_tex_line = _sage_const_623 
 _st_.plot(_sage_const_17 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_623 )
try:
 _st_.current_tex_line = _sage_const_624 
 _st_.plot(_sage_const_18 , format='notprovided', _p_=plot(g(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_624 )
try:
 _st_.current_tex_line = _sage_const_625 
 _st_.plot(_sage_const_19 , format='notprovided', _p_=plot(F(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_625 )
try:
 _st_.current_tex_line = _sage_const_638 
 _st_.plot(_sage_const_20 , format='notprovided', _p_=plot(arcsinh(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_638 )
_st_.current_tex_line = _sage_const_659 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsinh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_663 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_665 
 _st_.inline(_sage_const_37 , latex(f(x)))
except:
 _st_.goboom(_sage_const_665 )
try:
 _st_.current_tex_line = _sage_const_665 
 _st_.inline(_sage_const_38 , latex(g(x)))
except:
 _st_.goboom(_sage_const_665 )
try:
 _st_.current_tex_line = _sage_const_682 
 _st_.inline(_sage_const_39 , latex(f(x)))
except:
 _st_.goboom(_sage_const_682 )
try:
 _st_.current_tex_line = _sage_const_682 
 _st_.inline(_sage_const_40 , latex(F(x)))
except:
 _st_.goboom(_sage_const_682 )
try:
 _st_.current_tex_line = _sage_const_685 
 _st_.plot(_sage_const_21 , format='notprovided', _p_=plot(f(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_685 )
try:
 _st_.current_tex_line = _sage_const_686 
 _st_.plot(_sage_const_22 , format='notprovided', _p_=plot(g(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_686 )
try:
 _st_.current_tex_line = _sage_const_687 
 _st_.plot(_sage_const_23 , format='notprovided', _p_=plot(F(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_687 )
try:
 _st_.current_tex_line = _sage_const_698 
 _st_.plot(_sage_const_24 , format='notprovided', _p_=plot(arctanh(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_698 )
_st_.current_tex_line = _sage_const_721 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctanh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_725 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_727 
 _st_.inline(_sage_const_41 , latex(f(x)))
except:
 _st_.goboom(_sage_const_727 )
try:
 _st_.current_tex_line = _sage_const_727 
 _st_.inline(_sage_const_42 , latex(g(x)))
except:
 _st_.goboom(_sage_const_727 )
try:
 _st_.current_tex_line = _sage_const_743 
 _st_.inline(_sage_const_43 , latex(f(x)))
except:
 _st_.goboom(_sage_const_743 )
try:
 _st_.current_tex_line = _sage_const_743 
 _st_.inline(_sage_const_44 , latex(F(x)))
except:
 _st_.goboom(_sage_const_743 )
try:
 _st_.current_tex_line = _sage_const_746 
 _st_.plot(_sage_const_25 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_746 )
try:
 _st_.current_tex_line = _sage_const_747 
 _st_.plot(_sage_const_26 , format='notprovided', _p_=plot(g(x), x, -_sage_const_0p9 , _sage_const_0p9 ))
except:
 _st_.goboom(_sage_const_747 )
try:
 _st_.current_tex_line = _sage_const_748 
 _st_.plot(_sage_const_27 , format='notprovided', _p_=plot(F(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_748 )
_st_.current_tex_line = _sage_const_840 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(ln(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_843 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_845 
 _st_.inline(_sage_const_45 , latex(f(x)))
except:
 _st_.goboom(_sage_const_845 )
try:
 _st_.current_tex_line = _sage_const_845 
 _st_.inline(_sage_const_46 , latex(g(x)))
except:
 _st_.goboom(_sage_const_845 )
try:
 _st_.current_tex_line = _sage_const_847 
 _st_.inline(_sage_const_47 , latex(f(x)))
except:
 _st_.goboom(_sage_const_847 )
try:
 _st_.current_tex_line = _sage_const_851 
 _st_.plot(_sage_const_28 , format='notprovided', _p_=plot(f(x), x, _sage_const_0 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_851 )
_st_.current_tex_line = _sage_const_877 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(log(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_880 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_882 
 _st_.inline(_sage_const_48 , latex(f(x)))
except:
 _st_.goboom(_sage_const_882 )
try:
 _st_.current_tex_line = _sage_const_882 
 _st_.inline(_sage_const_49 , latex(F(x)))
except:
 _st_.goboom(_sage_const_882 )
try:
 _st_.current_tex_line = _sage_const_902 
 _st_.plot(_sage_const_29 , format='notprovided', _p_=plot(x+sqrt(x**_sage_const_2 -_sage_const_1 ), x, -_sage_const_5 , -_sage_const_1 ))
except:
 _st_.goboom(_sage_const_902 )
try:
 _st_.current_tex_line = _sage_const_903 
 _st_.plot(_sage_const_30 , format='notprovided', _p_=plot(diff(x+sqrt(x**_sage_const_2 -_sage_const_1 ),x), x, -_sage_const_5 , -_sage_const_1 ))
except:
 _st_.goboom(_sage_const_903 )
try:
 _st_.current_tex_line = _sage_const_909 
 _st_.plot(_sage_const_31 , format='notprovided', _p_=plot(x+sqrt(x**_sage_const_2 -_sage_const_1 ), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_909 )
try:
 _st_.current_tex_line = _sage_const_910 
 _st_.plot(_sage_const_32 , format='notprovided', _p_=plot(diff(x+sqrt(x**_sage_const_2 -_sage_const_1 ),x), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_910 )
try:
 _st_.current_tex_line = _sage_const_953 
 _st_.plot(_sage_const_33 , format='notprovided', _p_=plot((x+sqrt(x**_sage_const_2 -_sage_const_1 )), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_953 )
try:
 _st_.current_tex_line = _sage_const_955 
 _st_.plot(_sage_const_34 , format='notprovided', _p_=plot((x-sqrt(x**_sage_const_2 -_sage_const_1 )), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_955 )
try:
 _st_.current_tex_line = _sage_const_958 
 _st_.plot(_sage_const_35 , format='notprovided', _p_=plot(arccosh(x), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_958 )
try:
 _st_.current_tex_line = _sage_const_959 
 _st_.plot(_sage_const_36 , format='notprovided', _p_=plot(log(x+sqrt(x**_sage_const_2 -_sage_const_1 )), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_959 )
try:
 _st_.current_tex_line = _sage_const_960 
 _st_.plot(_sage_const_37 , format='notprovided', _p_=plot(log(x-sqrt(x**_sage_const_2 -_sage_const_1 )), x, _sage_const_1 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_960 )
try:
 _st_.current_tex_line = _sage_const_978 
 _st_.plot(_sage_const_38 , format='notprovided', _p_=plot(x+sqrt(x**_sage_const_2 +_sage_const_1 ), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_978 )
try:
 _st_.current_tex_line = _sage_const_979 
 _st_.plot(_sage_const_39 , format='notprovided', _p_=plot(diff(x+sqrt(x**_sage_const_2 +_sage_const_1 ),x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_979 )
try:
 _st_.current_tex_line = _sage_const_1012 
 _st_.plot(_sage_const_40 , format='notprovided', _p_=plot(log(x+sqrt(x**_sage_const_2 +_sage_const_1 )), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_1012 )
try:
 _st_.current_tex_line = _sage_const_1014 
 _st_.plot(_sage_const_41 , format='notprovided', _p_=plot(arcsinh(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_1014 )
_st_.endofdoc()

