from pomegranate import *

age = DiscreteDistribution( { '0':0.5, '1':0.5 } )
political_inclination = DiscreteDistribution( { '0':0.5, '1':0.5 } )

gun = ConditionalProbabilityTable(
        [[ '0', '0', 0.3 ],
         [ '0', '1', 0.7 ],
         [ '1', '0', 0.6 ],
         [ '1', '1', 0.4 ],
         [age] )

immigration = ConditionalProbabilityTable(
        [[ '0', '0', 0.25 ],
         [ '0', '1', 0.75 ],
         [ '1', '0', 0.20 ],
         [ '1', '1', 0.80 ],
         [age] )

voting = ConditionalProbabilityTable(
        [[ '0', '0', '0', 0.3 ],
         [ '0', '1', '0', 0.5 ],
         [ '1', '0', '0', 0.8 ],
         [ '1', '1', '0', 0.6 ],
         [ '0', '0', '1', 0.7 ],
         [ '0', '1', '1', 0.5 ],
         [ '1', '0', '1', 0.2 ],
         [ '1', '1', '1', 0.4 ]],
         [gun, immigration] )

drug = ConditionalProbabilityTable(
        [[ '0', '0', '0', 0.45 ],
         [ '0', '1', '0', 0.75 ],
         [ '1', '0', '0', 0.30 ],
         [ '1', '1', '0', 0.15 ],
         [ '0', '0', '1', 0.55 ],
         [ '0', '1', '1', 0.25 ],
         [ '1', '0', '1', 0.70 ],
         [ '1', '1', '1', 0.85 ]],
         [political_inclination, age] )
