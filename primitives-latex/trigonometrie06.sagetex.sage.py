## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file trigonometrie06.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_209 = Integer(209); _sage_const_213 = Integer(213); _sage_const_215 = Integer(215); _sage_const_0 = Integer(0); _sage_const_232 = Integer(232); _sage_const_1 = Integer(1); _sage_const_238 = Integer(238); _sage_const_242 = Integer(242); _sage_const_246 = Integer(246); _sage_const_263 = Integer(263); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_269 = Integer(269); _sage_const_273 = Integer(273); _sage_const_276 = Integer(276); _sage_const_1p4 = RealNumber('1.4'); _sage_const_291 = Integer(291); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_302 = Integer(302); _sage_const_6 = Integer(6); _sage_const_7 = Integer(7); _sage_const_314 = Integer(314); _sage_const_318 = Integer(318); _sage_const_329 = Integer(329); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_333 = Integer(333); _sage_const_334 = Integer(334); _sage_const_335 = Integer(335); _sage_const_10 = Integer(10); _sage_const_348 = Integer(348); _sage_const_11 = Integer(11); _sage_const_12 = Integer(12); _sage_const_356 = Integer(356); _sage_const_360 = Integer(360); _sage_const_371 = Integer(371); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_375 = Integer(375); _sage_const_376 = Integer(376); _sage_const_377 = Integer(377); _sage_const_15 = Integer(15); _sage_const_391 = Integer(391); _sage_const_16 = Integer(16); _sage_const_17 = Integer(17); _sage_const_403 = Integer(403); _sage_const_407 = Integer(407); _sage_const_414 = Integer(414); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_417 = Integer(417); _sage_const_418 = Integer(418); _sage_const_419 = Integer(419); _sage_const_20 = Integer(20); _sage_const_434 = Integer(434); _sage_const_21 = Integer(21); _sage_const_22 = Integer(22); _sage_const_451 = Integer(451); _sage_const_455 = Integer(455); _sage_const_460 = Integer(460); _sage_const_461 = Integer(461); _sage_const_462 = Integer(462); _sage_const_23 = Integer(23); _sage_const_476 = Integer(476); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_485 = Integer(485); _sage_const_489 = Integer(489); _sage_const_492 = Integer(492); _sage_const_493 = Integer(493); _sage_const_494 = Integer(494); _sage_const_26 = Integer(26); _sage_const_510 = Integer(510); _sage_const_27 = Integer(27); _sage_const_28 = Integer(28); _sage_const_517 = Integer(517); _sage_const_521 = Integer(521); _sage_const_525 = Integer(525); _sage_const_526 = Integer(526); _sage_const_527 = Integer(527); _sage_const_29 = Integer(29); _sage_const_548 = Integer(548); _sage_const_30 = Integer(30); _sage_const_31 = Integer(31); _sage_const_558 = Integer(558); _sage_const_562 = Integer(562); _sage_const_570 = Integer(570); _sage_const_589 = Integer(589); _sage_const_32 = Integer(32); _sage_const_33 = Integer(33); _sage_const_603 = Integer(603); _sage_const_34 = Integer(34); _sage_const_35 = Integer(35); _sage_const_606 = Integer(606); _sage_const_607 = Integer(607); _sage_const_608 = Integer(608); _sage_const_617 = Integer(617); _sage_const_621 = Integer(621); _sage_const_628 = Integer(628); _sage_const_646 = Integer(646); _sage_const_36 = Integer(36); _sage_const_37 = Integer(37); _sage_const_658 = Integer(658); _sage_const_38 = Integer(38); _sage_const_39 = Integer(39); _sage_const_661 = Integer(661); _sage_const_662 = Integer(662); _sage_const_663 = Integer(663); _sage_const_670 = Integer(670); _sage_const_674 = Integer(674); _sage_const_680 = Integer(680); _sage_const_698 = Integer(698); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_714 = Integer(714); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_717 = Integer(717); _sage_const_718 = Integer(718); _sage_const_0p9 = RealNumber('0.9'); _sage_const_719 = Integer(719); _sage_const_780 = Integer(780); _sage_const_784 = Integer(784); _sage_const_802 = Integer(802); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_804 = Integer(804); _sage_const_824 = Integer(824); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_836 = Integer(836); _sage_const_837 = Integer(837); _sage_const_870 = Integer(870); _sage_const_872 = Integer(872); _sage_const_901 = Integer(901); _sage_const_902 = Integer(902); _sage_const_944 = Integer(944); _sage_const_946 = Integer(946)## This file (trigonometrie06.sagetex.sage) was *autogenerated* from trigonometrie06.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('trigonometrie06', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_209 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_213 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_215 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=plot(cos(x), x, -pi, pi))
except:
 _st_.goboom(_sage_const_215 )
try:
 _st_.current_tex_line = _sage_const_232 
 _st_.inline(_sage_const_0 , latex(f(x)))
except:
 _st_.goboom(_sage_const_232 )
try:
 _st_.current_tex_line = _sage_const_232 
 _st_.inline(_sage_const_1 , latex(F(x)))
except:
 _st_.goboom(_sage_const_232 )
_st_.current_tex_line = _sage_const_238 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_242 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_246 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=plot(sin(x), x, -pi, pi))
except:
 _st_.goboom(_sage_const_246 )
try:
 _st_.current_tex_line = _sage_const_263 
 _st_.inline(_sage_const_2 , latex(f(x)))
except:
 _st_.goboom(_sage_const_263 )
try:
 _st_.current_tex_line = _sage_const_263 
 _st_.inline(_sage_const_3 , latex(F(x)))
except:
 _st_.goboom(_sage_const_263 )
_st_.current_tex_line = _sage_const_269 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_273 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=plot(tan(x), x, -_sage_const_1p4 , _sage_const_1p4 ))
except:
 _st_.goboom(_sage_const_276 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.inline(_sage_const_4 , latex(f(x)))
except:
 _st_.goboom(_sage_const_291 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.inline(_sage_const_5 , latex(g(x)))
except:
 _st_.goboom(_sage_const_291 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_6 , latex(f(x)))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_7 , latex(F(x)))
except:
 _st_.goboom(_sage_const_302 )
_st_.current_tex_line = _sage_const_314 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_318 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_329 
 _st_.inline(_sage_const_8 , latex(f(x)))
except:
 _st_.goboom(_sage_const_329 )
try:
 _st_.current_tex_line = _sage_const_329 
 _st_.inline(_sage_const_9 , latex(g(x)))
except:
 _st_.goboom(_sage_const_329 )
try:
 _st_.current_tex_line = _sage_const_333 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_333 )
try:
 _st_.current_tex_line = _sage_const_334 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=plot(cos(x), x, _sage_const_0 , pi))
except:
 _st_.goboom(_sage_const_334 )
try:
 _st_.current_tex_line = _sage_const_335 
 _st_.inline(_sage_const_10 , latex(f(x)))
except:
 _st_.goboom(_sage_const_335 )
try:
 _st_.current_tex_line = _sage_const_348 
 _st_.inline(_sage_const_11 , latex(f(x)))
except:
 _st_.goboom(_sage_const_348 )
try:
 _st_.current_tex_line = _sage_const_348 
 _st_.inline(_sage_const_12 , latex(F(x)))
except:
 _st_.goboom(_sage_const_348 )
_st_.current_tex_line = _sage_const_356 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_360 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_371 
 _st_.inline(_sage_const_13 , latex(f(x)))
except:
 _st_.goboom(_sage_const_371 )
try:
 _st_.current_tex_line = _sage_const_371 
 _st_.inline(_sage_const_14 , latex(g(x)))
except:
 _st_.goboom(_sage_const_371 )
try:
 _st_.current_tex_line = _sage_const_375 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_375 )
try:
 _st_.current_tex_line = _sage_const_376 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=plot(sin(x), x, -pi/_sage_const_2 , pi/_sage_const_2 ))
except:
 _st_.goboom(_sage_const_376 )
try:
 _st_.current_tex_line = _sage_const_377 
 _st_.inline(_sage_const_15 , latex(f(x)))
except:
 _st_.goboom(_sage_const_377 )
try:
 _st_.current_tex_line = _sage_const_391 
 _st_.inline(_sage_const_16 , latex(f(x)))
except:
 _st_.goboom(_sage_const_391 )
try:
 _st_.current_tex_line = _sage_const_391 
 _st_.inline(_sage_const_17 , latex(F(x)))
except:
 _st_.goboom(_sage_const_391 )
_st_.current_tex_line = _sage_const_403 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_407 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_414 
 _st_.inline(_sage_const_18 , latex(f(x)))
except:
 _st_.goboom(_sage_const_414 )
try:
 _st_.current_tex_line = _sage_const_414 
 _st_.inline(_sage_const_19 , latex(g(x)))
except:
 _st_.goboom(_sage_const_414 )
try:
 _st_.current_tex_line = _sage_const_417 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(f(x), x, -_sage_const_10 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_417 )
try:
 _st_.current_tex_line = _sage_const_418 
 _st_.plot(_sage_const_8 , format='notprovided', _p_=plot(tan(x), x, -_sage_const_1p4 , _sage_const_1p4 ))
except:
 _st_.goboom(_sage_const_418 )
try:
 _st_.current_tex_line = _sage_const_419 
 _st_.inline(_sage_const_20 , latex(f(x)))
except:
 _st_.goboom(_sage_const_419 )
try:
 _st_.current_tex_line = _sage_const_434 
 _st_.inline(_sage_const_21 , latex(f(x)))
except:
 _st_.goboom(_sage_const_434 )
try:
 _st_.current_tex_line = _sage_const_434 
 _st_.inline(_sage_const_22 , latex(F(x)))
except:
 _st_.goboom(_sage_const_434 )
_st_.current_tex_line = _sage_const_451 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cosh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_455 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_460 
 _st_.plot(_sage_const_9 , format='notprovided', _p_=plot(f(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_460 )
try:
 _st_.current_tex_line = _sage_const_461 
 _st_.plot(_sage_const_10 , format='notprovided', _p_=plot(g(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_461 )
try:
 _st_.current_tex_line = _sage_const_462 
 _st_.inline(_sage_const_23 , latex(f(x)))
except:
 _st_.goboom(_sage_const_462 )
try:
 _st_.current_tex_line = _sage_const_476 
 _st_.inline(_sage_const_24 , latex(f(x)))
except:
 _st_.goboom(_sage_const_476 )
try:
 _st_.current_tex_line = _sage_const_476 
 _st_.inline(_sage_const_25 , latex(F(x)))
except:
 _st_.goboom(_sage_const_476 )
_st_.current_tex_line = _sage_const_485 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sinh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_489 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_492 
 _st_.plot(_sage_const_11 , format='notprovided', _p_=plot(f(x), x, -_sage_const_3 , _sage_const_3 ))
except:
 _st_.goboom(_sage_const_492 )
try:
 _st_.current_tex_line = _sage_const_493 
 _st_.plot(_sage_const_12 , format='notprovided', _p_=plot(g(x), x, -_sage_const_3 , _sage_const_3 ))
except:
 _st_.goboom(_sage_const_493 )
try:
 _st_.current_tex_line = _sage_const_494 
 _st_.inline(_sage_const_26 , latex(sinh(x)))
except:
 _st_.goboom(_sage_const_494 )
try:
 _st_.current_tex_line = _sage_const_510 
 _st_.inline(_sage_const_27 , latex(f(x)))
except:
 _st_.goboom(_sage_const_510 )
try:
 _st_.current_tex_line = _sage_const_510 
 _st_.inline(_sage_const_28 , latex(F(x)))
except:
 _st_.goboom(_sage_const_510 )
_st_.current_tex_line = _sage_const_517 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tanh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_521 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_525 
 _st_.plot(_sage_const_13 , format='notprovided', _p_=plot(f(x), x, -_sage_const_3 , _sage_const_3 ))
except:
 _st_.goboom(_sage_const_525 )
try:
 _st_.current_tex_line = _sage_const_526 
 _st_.plot(_sage_const_14 , format='notprovided', _p_=plot(g(x), x, -_sage_const_3 , _sage_const_3 ))
except:
 _st_.goboom(_sage_const_526 )
try:
 _st_.current_tex_line = _sage_const_527 
 _st_.inline(_sage_const_29 , latex(f(x)))
except:
 _st_.goboom(_sage_const_527 )
try:
 _st_.current_tex_line = _sage_const_548 
 _st_.inline(_sage_const_30 , latex(f(x)))
except:
 _st_.goboom(_sage_const_548 )
try:
 _st_.current_tex_line = _sage_const_548 
 _st_.inline(_sage_const_31 , latex(F(x)))
except:
 _st_.goboom(_sage_const_548 )
_st_.current_tex_line = _sage_const_558 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccosh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_562 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_570 
 _st_.plot(_sage_const_15 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_570 )
try:
 _st_.current_tex_line = _sage_const_589 
 _st_.inline(_sage_const_32 , latex(f(x)))
except:
 _st_.goboom(_sage_const_589 )
try:
 _st_.current_tex_line = _sage_const_589 
 _st_.inline(_sage_const_33 , latex(g(x)))
except:
 _st_.goboom(_sage_const_589 )
try:
 _st_.current_tex_line = _sage_const_603 
 _st_.inline(_sage_const_34 , latex(f(x)))
except:
 _st_.goboom(_sage_const_603 )
try:
 _st_.current_tex_line = _sage_const_603 
 _st_.inline(_sage_const_35 , latex(F(x)))
except:
 _st_.goboom(_sage_const_603 )
try:
 _st_.current_tex_line = _sage_const_606 
 _st_.plot(_sage_const_16 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_606 )
try:
 _st_.current_tex_line = _sage_const_607 
 _st_.plot(_sage_const_17 , format='notprovided', _p_=plot(g(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_607 )
try:
 _st_.current_tex_line = _sage_const_608 
 _st_.plot(_sage_const_18 , format='notprovided', _p_=plot(F(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_608 )
_st_.current_tex_line = _sage_const_617 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsinh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_621 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_628 
 _st_.plot(_sage_const_19 , format='notprovided', _p_=plot(arcsinh(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_628 )
try:
 _st_.current_tex_line = _sage_const_646 
 _st_.inline(_sage_const_36 , latex(f(x)))
except:
 _st_.goboom(_sage_const_646 )
try:
 _st_.current_tex_line = _sage_const_646 
 _st_.inline(_sage_const_37 , latex(g(x)))
except:
 _st_.goboom(_sage_const_646 )
try:
 _st_.current_tex_line = _sage_const_658 
 _st_.inline(_sage_const_38 , latex(f(x)))
except:
 _st_.goboom(_sage_const_658 )
try:
 _st_.current_tex_line = _sage_const_658 
 _st_.inline(_sage_const_39 , latex(F(x)))
except:
 _st_.goboom(_sage_const_658 )
try:
 _st_.current_tex_line = _sage_const_661 
 _st_.plot(_sage_const_20 , format='notprovided', _p_=plot(f(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_661 )
try:
 _st_.current_tex_line = _sage_const_662 
 _st_.plot(_sage_const_21 , format='notprovided', _p_=plot(g(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_662 )
try:
 _st_.current_tex_line = _sage_const_663 
 _st_.plot(_sage_const_22 , format='notprovided', _p_=plot(F(x), x, -_sage_const_20 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_663 )
_st_.current_tex_line = _sage_const_670 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctanh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_674 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_680 
 _st_.plot(_sage_const_23 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_680 )
try:
 _st_.current_tex_line = _sage_const_698 
 _st_.inline(_sage_const_40 , latex(f(x)))
except:
 _st_.goboom(_sage_const_698 )
try:
 _st_.current_tex_line = _sage_const_698 
 _st_.inline(_sage_const_41 , latex(g(x)))
except:
 _st_.goboom(_sage_const_698 )
try:
 _st_.current_tex_line = _sage_const_714 
 _st_.inline(_sage_const_42 , latex(f(x)))
except:
 _st_.goboom(_sage_const_714 )
try:
 _st_.current_tex_line = _sage_const_714 
 _st_.inline(_sage_const_43 , latex(F(x)))
except:
 _st_.goboom(_sage_const_714 )
try:
 _st_.current_tex_line = _sage_const_717 
 _st_.plot(_sage_const_24 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_717 )
try:
 _st_.current_tex_line = _sage_const_718 
 _st_.plot(_sage_const_25 , format='notprovided', _p_=plot(g(x), x, -_sage_const_0p9 , _sage_const_0p9 ))
except:
 _st_.goboom(_sage_const_718 )
try:
 _st_.current_tex_line = _sage_const_719 
 _st_.plot(_sage_const_26 , format='notprovided', _p_=plot(F(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_719 )
_st_.current_tex_line = _sage_const_780 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(ln(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_784 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_802 
 _st_.inline(_sage_const_44 , latex(f(x)))
except:
 _st_.goboom(_sage_const_802 )
try:
 _st_.current_tex_line = _sage_const_802 
 _st_.inline(_sage_const_45 , latex(g(x)))
except:
 _st_.goboom(_sage_const_802 )
try:
 _st_.current_tex_line = _sage_const_804 
 _st_.plot(_sage_const_27 , format='notprovided', _p_=plot(f(x), x, _sage_const_0 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_804 )
try:
 _st_.current_tex_line = _sage_const_824 
 _st_.inline(_sage_const_46 , latex(f(x)))
except:
 _st_.goboom(_sage_const_824 )
try:
 _st_.current_tex_line = _sage_const_824 
 _st_.inline(_sage_const_47 , latex(F(x)))
except:
 _st_.goboom(_sage_const_824 )
try:
 _st_.current_tex_line = _sage_const_836 
 _st_.plot(_sage_const_28 , format='notprovided', _p_=plot(x+sqrt(x**_sage_const_2 +_sage_const_1 ), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_836 )
try:
 _st_.current_tex_line = _sage_const_837 
 _st_.plot(_sage_const_29 , format='notprovided', _p_=plot(diff(x+sqrt(x**_sage_const_2 +_sage_const_1 ),x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_837 )
try:
 _st_.current_tex_line = _sage_const_870 
 _st_.plot(_sage_const_30 , format='notprovided', _p_=plot(log(x+sqrt(x**_sage_const_2 +_sage_const_1 )), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_870 )
try:
 _st_.current_tex_line = _sage_const_872 
 _st_.plot(_sage_const_31 , format='notprovided', _p_=plot(arcsinh(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_872 )
try:
 _st_.current_tex_line = _sage_const_901 
 _st_.plot(_sage_const_32 , format='notprovided', _p_=plot(x+sqrt(x**_sage_const_2  - _sage_const_1 ), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_901 )
try:
 _st_.current_tex_line = _sage_const_902 
 _st_.plot(_sage_const_33 , format='notprovided', _p_=plot(diff(x+sqrt(x**_sage_const_2  - _sage_const_1 ),x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_902 )
try:
 _st_.current_tex_line = _sage_const_944 
 _st_.plot(_sage_const_34 , format='notprovided', _p_=plot(log(x+sqrt(x**_sage_const_2 -_sage_const_1 )), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_944 )
try:
 _st_.current_tex_line = _sage_const_946 
 _st_.plot(_sage_const_35 , format='notprovided', _p_=plot(arccosh(x), x, -_sage_const_5 , _sage_const_5 ))
except:
 _st_.goboom(_sage_const_946 )
_st_.endofdoc()

