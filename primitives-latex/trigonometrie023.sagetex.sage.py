## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file trigonometrie023.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_230 = Integer(230); _sage_const_1 = Integer(1); _sage_const_233 = Integer(233); _sage_const_235 = Integer(235); _sage_const_0 = Integer(0); _sage_const_237 = Integer(237); _sage_const_2 = Integer(2); _sage_const_241 = Integer(241); _sage_const_267 = Integer(267); _sage_const_270 = Integer(270); _sage_const_272 = Integer(272); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_297 = Integer(297); _sage_const_300 = Integer(300); _sage_const_302 = Integer(302); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_305 = Integer(305); _sage_const_7 = Integer(7); _sage_const_309 = Integer(309); _sage_const_341 = Integer(341); _sage_const_344 = Integer(344); _sage_const_346 = Integer(346); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_373 = Integer(373); _sage_const_376 = Integer(376); _sage_const_378 = Integer(378); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_380 = Integer(380); _sage_const_12 = Integer(12); _sage_const_384 = Integer(384); _sage_const_420 = Integer(420); _sage_const_423 = Integer(423); _sage_const_425 = Integer(425); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_472 = Integer(472); _sage_const_475 = Integer(475); _sage_const_478 = Integer(478); _sage_const_15 = Integer(15); _sage_const_16 = Integer(16); _sage_const_480 = Integer(480); _sage_const_17 = Integer(17); _sage_const_484 = Integer(484); _sage_const_514 = Integer(514); _sage_const_517 = Integer(517); _sage_const_519 = Integer(519); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_543 = Integer(543); _sage_const_546 = Integer(546); _sage_const_549 = Integer(549); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_551 = Integer(551); _sage_const_22 = Integer(22); _sage_const_555 = Integer(555); _sage_const_586 = Integer(586); _sage_const_589 = Integer(589); _sage_const_592 = Integer(592); _sage_const_23 = Integer(23); _sage_const_24 = Integer(24); _sage_const_596 = Integer(596); _sage_const_25 = Integer(25); _sage_const_600 = Integer(600); _sage_const_635 = Integer(635); _sage_const_638 = Integer(638); _sage_const_641 = Integer(641); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_645 = Integer(645); _sage_const_28 = Integer(28); _sage_const_649 = Integer(649); _sage_const_723 = Integer(723); _sage_const_726 = Integer(726); _sage_const_728 = Integer(728); _sage_const_29 = Integer(29); _sage_const_30 = Integer(30); _sage_const_730 = Integer(730); _sage_const_31 = Integer(31); _sage_const_734 = Integer(734); _sage_const_768 = Integer(768); _sage_const_771 = Integer(771); _sage_const_773 = Integer(773); _sage_const_32 = Integer(32); _sage_const_33 = Integer(33)## This file (trigonometrie023.sagetex.sage) was *autogenerated* from trigonometrie023.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('trigonometrie023', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_230 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_233 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_0 , latex(f(x)))
except:
 _st_.goboom(_sage_const_235 )
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_1 , latex(g(x)))
except:
 _st_.goboom(_sage_const_235 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_2 , latex(f(x)))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_241 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_241 )
_st_.current_tex_line = _sage_const_267 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_270 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_272 
 _st_.inline(_sage_const_3 , latex(f(x)))
except:
 _st_.goboom(_sage_const_272 )
try:
 _st_.current_tex_line = _sage_const_272 
 _st_.inline(_sage_const_4 , latex(F(x)))
except:
 _st_.goboom(_sage_const_272 )
_st_.current_tex_line = _sage_const_297 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_300 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_5 , latex(f(x)))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.inline(_sage_const_6 , latex(g(x)))
except:
 _st_.goboom(_sage_const_302 )
try:
 _st_.current_tex_line = _sage_const_305 
 _st_.inline(_sage_const_7 , latex(f(x)))
except:
 _st_.goboom(_sage_const_305 )
try:
 _st_.current_tex_line = _sage_const_309 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_309 )
_st_.current_tex_line = _sage_const_341 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arcsin(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_344 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_346 
 _st_.inline(_sage_const_8 , latex(f(x)))
except:
 _st_.goboom(_sage_const_346 )
try:
 _st_.current_tex_line = _sage_const_346 
 _st_.inline(_sage_const_9 , latex(F(x)))
except:
 _st_.goboom(_sage_const_346 )
_st_.current_tex_line = _sage_const_373 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_376 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_378 
 _st_.inline(_sage_const_10 , latex(f(x)))
except:
 _st_.goboom(_sage_const_378 )
try:
 _st_.current_tex_line = _sage_const_378 
 _st_.inline(_sage_const_11 , latex(g(x)))
except:
 _st_.goboom(_sage_const_378 )
try:
 _st_.current_tex_line = _sage_const_380 
 _st_.inline(_sage_const_12 , latex(f(x)))
except:
 _st_.goboom(_sage_const_380 )
try:
 _st_.current_tex_line = _sage_const_384 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=plot(f(x), x, -_sage_const_10 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_384 )
_st_.current_tex_line = _sage_const_420 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arctan(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_423 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_425 
 _st_.inline(_sage_const_13 , latex(f(x)))
except:
 _st_.goboom(_sage_const_425 )
try:
 _st_.current_tex_line = _sage_const_425 
 _st_.inline(_sage_const_14 , latex(F(x)))
except:
 _st_.goboom(_sage_const_425 )
_st_.current_tex_line = _sage_const_472 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(sinh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_475 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_478 
 _st_.inline(_sage_const_15 , latex(f(x)))
except:
 _st_.goboom(_sage_const_478 )
try:
 _st_.current_tex_line = _sage_const_478 
 _st_.inline(_sage_const_16 , latex(F(x)))
except:
 _st_.goboom(_sage_const_478 )
try:
 _st_.current_tex_line = _sage_const_480 
 _st_.inline(_sage_const_17 , latex(f(x)))
except:
 _st_.goboom(_sage_const_480 )
try:
 _st_.current_tex_line = _sage_const_484 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_484 )
_st_.current_tex_line = _sage_const_514 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(tanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_517 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_519 
 _st_.inline(_sage_const_18 , latex(f(x)))
except:
 _st_.goboom(_sage_const_519 )
try:
 _st_.current_tex_line = _sage_const_519 
 _st_.inline(_sage_const_19 , latex(F(x)))
except:
 _st_.goboom(_sage_const_519 )
_st_.current_tex_line = _sage_const_543 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(acosh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_546 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_549 
 _st_.inline(_sage_const_20 , latex(f(x)))
except:
 _st_.goboom(_sage_const_549 )
try:
 _st_.current_tex_line = _sage_const_549 
 _st_.inline(_sage_const_21 , latex(F(x)))
except:
 _st_.goboom(_sage_const_549 )
try:
 _st_.current_tex_line = _sage_const_551 
 _st_.inline(_sage_const_22 , latex(f(x)))
except:
 _st_.goboom(_sage_const_551 )
try:
 _st_.current_tex_line = _sage_const_555 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_555 )
_st_.current_tex_line = _sage_const_586 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(asinh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_589 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_592 
 _st_.inline(_sage_const_23 , latex(f(x)))
except:
 _st_.goboom(_sage_const_592 )
try:
 _st_.current_tex_line = _sage_const_592 
 _st_.inline(_sage_const_24 , latex(F(x)))
except:
 _st_.goboom(_sage_const_592 )
try:
 _st_.current_tex_line = _sage_const_596 
 _st_.inline(_sage_const_25 , latex(f(x)))
except:
 _st_.goboom(_sage_const_596 )
try:
 _st_.current_tex_line = _sage_const_600 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_600 )
_st_.current_tex_line = _sage_const_635 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(atanh(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_638 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_641 
 _st_.inline(_sage_const_26 , latex(f(x)))
except:
 _st_.goboom(_sage_const_641 )
try:
 _st_.current_tex_line = _sage_const_641 
 _st_.inline(_sage_const_27 , latex(F(x)))
except:
 _st_.goboom(_sage_const_641 )
try:
 _st_.current_tex_line = _sage_const_645 
 _st_.inline(_sage_const_28 , latex(f(x)))
except:
 _st_.goboom(_sage_const_645 )
try:
 _st_.current_tex_line = _sage_const_649 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_649 )
_st_.current_tex_line = _sage_const_723 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(ln(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x,_sage_const_1 )).function(x)
except:
 _st_.goboom(_sage_const_726 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_728 
 _st_.inline(_sage_const_29 , latex(f(x)))
except:
 _st_.goboom(_sage_const_728 )
try:
 _st_.current_tex_line = _sage_const_728 
 _st_.inline(_sage_const_30 , latex(g(x)))
except:
 _st_.goboom(_sage_const_728 )
try:
 _st_.current_tex_line = _sage_const_730 
 _st_.inline(_sage_const_31 , latex(f(x)))
except:
 _st_.goboom(_sage_const_730 )
try:
 _st_.current_tex_line = _sage_const_734 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(f(x), x, _sage_const_0 , _sage_const_10 ))
except:
 _st_.goboom(_sage_const_734 )
_st_.current_tex_line = _sage_const_768 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(log(x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_771 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_773 
 _st_.inline(_sage_const_32 , latex(f(x)))
except:
 _st_.goboom(_sage_const_773 )
try:
 _st_.current_tex_line = _sage_const_773 
 _st_.inline(_sage_const_33 , latex(F(x)))
except:
 _st_.goboom(_sage_const_773 )
_st_.endofdoc()

