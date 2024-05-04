## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file trigonometrie-fonction-cos.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_154 = Integer(154); _sage_const_158 = Integer(158); _sage_const_160 = Integer(160); _sage_const_0 = Integer(0); _sage_const_177 = Integer(177); _sage_const_1 = Integer(1); _sage_const_186 = Integer(186); _sage_const_190 = Integer(190); _sage_const_201 = Integer(201); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_205 = Integer(205); _sage_const_206 = Integer(206); _sage_const_207 = Integer(207); _sage_const_4 = Integer(4); _sage_const_220 = Integer(220); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_230 = Integer(230); _sage_const_234 = Integer(234); _sage_const_239 = Integer(239); _sage_const_240 = Integer(240); _sage_const_241 = Integer(241); _sage_const_7 = Integer(7); _sage_const_255 = Integer(255); _sage_const_8 = Integer(8); _sage_const_9 = Integer(9); _sage_const_267 = Integer(267); _sage_const_271 = Integer(271); _sage_const_279 = Integer(279); _sage_const_20 = Integer(20); _sage_const_298 = Integer(298); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_312 = Integer(312); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_315 = Integer(315); _sage_const_316 = Integer(316); _sage_const_317 = Integer(317)## This file (trigonometrie-fonction-cos.sagetex.sage) was *autogenerated* from trigonometrie-fonction-cos.tex with sagetex.sty version 2021/10/16 v3.6.
import sagetex
_st_ = sagetex.SageTeXProcessor('trigonometrie-fonction-cos', version='2021/10/16 v3.6', version_check=True)
_st_.current_tex_line = _sage_const_154 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_158 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_160 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=plot(cos(x), x, -pi, pi))
except:
 _st_.goboom(_sage_const_160 )
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
_st_.current_tex_line = _sage_const_186 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccos(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_190 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_2 , latex(f(x)))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_3 , latex(g(x)))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_205 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=plot(f(x), x, -_sage_const_1 , _sage_const_1 ))
except:
 _st_.goboom(_sage_const_205 )
try:
 _st_.current_tex_line = _sage_const_206 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=plot(cos(x), x, _sage_const_0 , pi))
except:
 _st_.goboom(_sage_const_206 )
try:
 _st_.current_tex_line = _sage_const_207 
 _st_.inline(_sage_const_4 , latex(f(x)))
except:
 _st_.goboom(_sage_const_207 )
try:
 _st_.current_tex_line = _sage_const_220 
 _st_.inline(_sage_const_5 , latex(f(x)))
except:
 _st_.goboom(_sage_const_220 )
try:
 _st_.current_tex_line = _sage_const_220 
 _st_.inline(_sage_const_6 , latex(F(x)))
except:
 _st_.goboom(_sage_const_220 )
_st_.current_tex_line = _sage_const_230 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(cosh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_234 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_239 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=plot(f(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_239 )
try:
 _st_.current_tex_line = _sage_const_240 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=plot(g(x), x, -_sage_const_4 , _sage_const_4 ))
except:
 _st_.goboom(_sage_const_240 )
try:
 _st_.current_tex_line = _sage_const_241 
 _st_.inline(_sage_const_7 , latex(f(x)))
except:
 _st_.goboom(_sage_const_241 )
try:
 _st_.current_tex_line = _sage_const_255 
 _st_.inline(_sage_const_8 , latex(f(x)))
except:
 _st_.goboom(_sage_const_255 )
try:
 _st_.current_tex_line = _sage_const_255 
 _st_.inline(_sage_const_9 , latex(F(x)))
except:
 _st_.goboom(_sage_const_255 )
_st_.current_tex_line = _sage_const_267 
_st_.blockbegin()
try:
     __tmp__=var("x"); f = symbolic_expression(arccosh(x)).function(x)
     __tmp__=var("x"); g = symbolic_expression(diff(f(x),x)).function(x)
     __tmp__=var("x"); F = symbolic_expression(integrate(f(x),x)).function(x)
except:
 _st_.goboom(_sage_const_271 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_279 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_279 )
try:
 _st_.current_tex_line = _sage_const_298 
 _st_.inline(_sage_const_10 , latex(f(x)))
except:
 _st_.goboom(_sage_const_298 )
try:
 _st_.current_tex_line = _sage_const_298 
 _st_.inline(_sage_const_11 , latex(g(x)))
except:
 _st_.goboom(_sage_const_298 )
try:
 _st_.current_tex_line = _sage_const_312 
 _st_.inline(_sage_const_12 , latex(f(x)))
except:
 _st_.goboom(_sage_const_312 )
try:
 _st_.current_tex_line = _sage_const_312 
 _st_.inline(_sage_const_13 , latex(F(x)))
except:
 _st_.goboom(_sage_const_312 )
try:
 _st_.current_tex_line = _sage_const_315 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=plot(f(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_315 )
try:
 _st_.current_tex_line = _sage_const_316 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=plot(g(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_316 )
try:
 _st_.current_tex_line = _sage_const_317 
 _st_.plot(_sage_const_8 , format='notprovided', _p_=plot(F(x), x, _sage_const_1 , _sage_const_20 ))
except:
 _st_.goboom(_sage_const_317 )
_st_.endofdoc()
