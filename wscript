#! /usr/bin/env python
# encoding: utf-8

top = '.'
out = 'build'


def options(opt):
	opt.load('compiler_cxx')

def configure(conf):
	conf.load('compiler_cxx')
	conf.load('waf_conan_libs_info', tooldir='.')
	conf.load('waf_conan_toolchain', tooldir='.')

def build(bld):
	bld.stlib(target='mylib', source='./src/mylib.cpp')
