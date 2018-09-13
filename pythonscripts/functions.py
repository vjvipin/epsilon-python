#!/bin/python

#def function(arg):
# print(arg)
#
#arg1 = "argument 1"
#arg2 = "argument 2"
#function(arg1)
#function(arg2)
#
#Keyowrd  arguments
#def function(arg1, arg2):
#    print(arg1, arg2)

#default positional argument
def function(arg1 = "default arg1" ,  arg2 = "argument 2", arg3 = "argumnet 3" ):
    print(arg1)
    print(arg2)
    print(arg3)
arg1 = "argument 1"
arg2 = "my argument"
arg3 = "my argument 3"
#function(arg1,arg3, arg2)
function()
function(arg1)
function(arg1,arg2)
function("only argument ", "2nd argument")


