from netfilter.rule import Rule,Match

from netfilter.table import Table


x = 0
while x== 0 :
	table_name = input('table_name : ')
	chain_name = input('chain_name : ')

	rule = Rule(

	    in_interface=input('in_interface : '),

	    protocol=input('protocol : '),

	    matches=[Match(input('name : '), '--dport '+input('dport : ') )],

	    jump=input('jump : '))



	table = Table(table_name)

	table.append_rule(chain_name, rule)
	y = input('Do you want Exit ?')
	if y == 'yes':
		x = 1