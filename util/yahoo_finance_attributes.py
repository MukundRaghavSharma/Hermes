import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

attributes = {

# Pricing Dividends #
# ----------------- #
'Ask' 											:  'a',
'Dividend Yield' 								:  'y', 
'Bid' 											:  'b',  
'Dividend per Share'							:  'd',
'Ask-Realtime'									: 'b2', 
'Dividend Pay Date'								: 'r1',
'Bid-Realtime'									: 'b3',
'Ex-Dividend Date'								:  'q',
'Previous Close'								:  'p',
'Open'											:  'o',	

# Dates #
# ----- #
'Change' 										: 'c1',	
'Last Trade Date'								: 'd1',
'Change & Percent Change'						:  'c',
'Trade Date'									: 'd2',
'Change-Realtime'								: 'c6',
'Last Trade Time'								: 't1',
'Change Percent-Realtime'						: 'k2',
'Change in Percent'								: 'p2',

# Averages #
# -------- #
'After Hours Change-Realtime'                   :  'm5',
'Change From 200 Day Moving Average'        	:  'c3', 
'Commission'	                                :  'm6',
'Percent Change From 200 Day Moving Average' 	:  	'g',
'Days Low'	                                	:  'm7',
'Change From 50 Day Moving Average'          	:  	'h',
'Days High'	                                    :  'm8',
'Percent Change From 50 Day Moving Average'  	:  'k1',
'Last Trade-Realtime-With Time'              	:  'm3',
'50 Day Moving Average'                      	:  	'l',
'Last Trade-With Time-'                      	:  'm4',
'200 Day Moving Average'                     	:  'l1',
'Last Trade-Price Only-'                     	:  't8',
'1 yr Target Price'

# Misc #
# ----- #
'Days Value Change'                            :  'w1',
'Holdings Gain Percent'                         :  'g1',
'Days Value Change (Realtime)'                 :  'w4',
'Annualized Gain'                           	:  'g3',
'Price Paid'                                	:  'p1',
'Holdings Gain'                             	:  'g4',
'Days Range'                               	:   'm', 
'Holdings Gain Percent (Realtime)'          	:  'g5',
'Days Range (Realtime)'                    	:  'm2',
'Holdings Gain (Realtime)'                  	:  'g6',

# 52 Week Pricing Symbol Info #
# --------------------------- #
'52 Week High'                                  :   'k',  
'More Info'                                     :   'v',  
'52 week Low'                                  	:   'j',  
'Market Capitalization'                        	:  'j1',
'Change From 52 Week Low'                      	:  'j5', 
'Market Cap (Realtime)'                        	:  'j3', 
'Change From 52 week High'                      :  'k4', 
'Float Shares'                                  :  'f6', 
'Percent Change From 52 week Low'               :  'j6',
'Name'                                          :   'n',  
'Percent Change From 52 week High'              :  'k5',
'Notes'                                         :  'n4', 
'52 week Range'                                 :   'w',  
'Symbol'                                        :   's',  
'Shares Owned'                                  :  's1', 
'Stock Exchange'                                :   'x',  
'Shares Outstanding'                            :  'j2', 

# Volume #
# ------ #
'Volume'                                        :   'v', 
'Ask Size'	                                    :  'a5',
'Bid Size'                                      : 'bi6',
'Last Trade Size'	                            :  'k3',
'Ticker Trend'                                  :  't7',
'Average Daily Volume'	                        :  'a2',
'Trade Links'                                   :  't6',
'Order Book (Realtime)'                         :  'i5',

# Ratios #
# ------ #
 'High Limit'                                   :  'l2',
 'Earnings per Share'                           :   'e',  
 'Low Limit'                                    :  'l3', 
 'EPS Estimate Current Year'                    :  'e7', 
 'Holdings Value'                               :  'v1', 
 'EPS Estimate Next Year'	                    :  'e8', 
 'Holdings Value (Realtime)'                    :  'v7', 
 'EPS Estimate Next Quarter'	                :  'e9', 
 'Revenue'                                      :  's6', 
 'Book Value'                                   :  'b4', 
 'EBITDA'                                       :  'j4', 
 'Price / Sales'                                :  'p5', 
 'Price / Book'                                 :  'p6', 
 'P/E Ratio'                                    :  'r' ,
 'P/E Ratio (Realtime)'                         :  'r2', 
 'PEG Ratio'                                    :  'r5', 
 'Price / EPS Estimate Current Year'            :  'r6', 
 'Price / EPS Estimate Next Year'               :  'r7', 
 'Short Ratio'                                  : 's7' 
}
