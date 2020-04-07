h = 0.70200; H0 = h*100; H0G = 0.07175 # units of 1/Gyr
G = 6.67408e-11
f = h5py.File(catdir+'m11q_res880/halo_600.hdf5','r')
omega_m = np.float64(f['cosmology:omega_matter'])
omega_l = np.float64(f['cosmology:omega_lambda'])
f_b = np.float(np.array(f['cosmology:baryon.fraction']))
f.close()

s=12  	#regular font size
ls=13 	#label font size
lw=2.5 	#line width
ms=7	#marker size
gs=11	#legend font size
ntl=3	#minor tick length
jtl=4	#major tick length
ts=11	#overlay text size
ra=-90	#text rotation angle
ms=4.5 #markersize
aph=0.7 #alpha
grey = '#727d8e'

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def get_snapnum(z):
	snapnums = np.array(['005',
		'006',
		'007',
		'008',
		'009',
		'010',
		'011',
		'012',
		'013',
		'014',
		'015',
		'016',
		'017',
		'018',
		'019',
		'020',
		'021',
		'022',
		'023',
		'024',
		'025',
		'026',
		'027',
		'028',
		'029',
		'030',
		'031',
		'032',
		'033',
		'034',
		'035',
		'036',
		'037',
		'038',
		'039',
		'040',
		'041',
		'042',
		'043',
		'044',
		'045',
		'046',
		'047',
		'048',
		'049',
		'050',
		'051',
		'052',
		'053',
		'054',
		'055',
		'056',
		'057',
		'058',
		'059',
		'060',
		'061',
		'062',
		'063',
		'064',
		'065',
		'066',
		'067',
		'068',
		'069',
		'070',
		'071',
		'072',
		'073',
		'074',
		'075',
		'076',
		'077',
		'078',
		'079',
		'080',
		'081',
		'082',
		'083',
		'084',
		'085',
		'086',
		'087',
		'088',
		'089',
		'090',
		'091',
		'092',
		'093',
		'094',
		'095',
		'096',
		'097',
		'098',
		'099',
		'100',
		'101',
		'102',
		'103',
		'104',
		'105',
		'106',
		'107',
		'108',
		'109',
		'110',
		'111',
		'112',
		'113',
		'114',
		'115',
		'116',
		'117',
		'118',
		'119',
		'120',
		'121',
		'122',
		'123',
		'124',
		'125',
		'126',
		'127',
		'128',
		'129',
		'130',
		'131',
		'132',
		'133',
		'134',
		'135',
		'136',
		'137',
		'138',
		'139',
		'140',
		'141',
		'142',
		'143',
		'144',
		'145',
		'146',
		'147',
		'148',
		'149',
		'150',
		'151',
		'152',
		'153',
		'154',
		'155',
		'156',
		'157',
		'158',
		'159',
		'160',
		'161',
		'162',
		'163',
		'164',
		'165',
		'166',
		'167',
		'168',
		'169',
		'170',
		'171',
		'172',
		'173',
		'174',
		'175',
		'176',
		'177',
		'178',
		'179',
		'180',
		'181',
		'182',
		'183',
		'184',
		'185',
		'186',
		'187',
		'188',
		'189',
		'190',
		'191',
		'192',
		'193',
		'194',
		'195',
		'196',
		'197',
		'198',
		'199',
		'200',
		'201',
		'202',
		'203',
		'204',
		'205',
		'206',
		'207',
		'208',
		'209',
		'210',
		'211',
		'212',
		'213',
		'214',
		'215',
		'216',
		'217',
		'218',
		'219',
		'220',
		'221',
		'222',
		'223',
		'224',
		'225',
		'226',
		'227',
		'228',
		'229',
		'230',
		'231',
		'232',
		'233',
		'234',
		'235',
		'236',
		'237',
		'238',
		'239',
		'240',
		'241',
		'242',
		'243',
		'244',
		'245',
		'246',
		'247',
		'248',
		'249',
		'250',
		'251',
		'252',
		'253',
		'254',
		'255',
		'256',
		'257',
		'258',
		'259',
		'260',
		'261',
		'262',
		'263',
		'264',
		'265',
		'266',
		'267',
		'268',
		'269',
		'270',
		'271',
		'272',
		'273',
		'274',
		'275',
		'276',
		'277',
		'278',
		'279',
		'280',
		'281',
		'282',
		'283',
		'284',
		'285',
		'286',
		'287',
		'288',
		'289',
		'290',
		'291',
		'292',
		'293',
		'294',
		'295',
		'296',
		'297',
		'298',
		'299',
		'300',
		'301',
		'302',
		'303',
		'304',
		'305',
		'306',
		'307',
		'308',
		'309',
		'310',
		'311',
		'312',
		'313',
		'314',
		'315',
		'316',
		'317',
		'318',
		'319',
		'320',
		'321',
		'322',
		'323',
		'324',
		'325',
		'326',
		'327',
		'328',
		'329',
		'330',
		'331',
		'332',
		'333',
		'334',
		'335',
		'336',
		'337',
		'338',
		'339',
		'340',
		'341',
		'342',
		'343',
		'344',
		'345',
		'346',
		'347',
		'348',
		'349',
		'350',
		'351',
		'352',
		'353',
		'354',
		'355',
		'356',
		'357',
		'358',
		'359',
		'360',
		'361',
		'362',
		'363',
		'364',
		'365',
		'366',
		'367',
		'368',
		'369',
		'370',
		'371',
		'372',
		'373',
		'374',
		'375',
		'376',
		'377',
		'378',
		'379',
		'380',
		'381',
		'382',
		'383',
		'384',
		'385',
		'386',
		'387',
		'388',
		'389',
		'390',
		'391',
		'392',
		'393',
		'394',
		'395',
		'396',
		'397',
		'398',
		'399',
		'400',
		'401',
		'402',
		'403',
		'404',
		'405',
		'406',
		'407',
		'408',
		'409',
		'410',
		'411',
		'412',
		'413',
		'414',
		'415',
		'416',
		'417',
		'418',
		'419',
		'420',
		'421',
		'422',
		'423',
		'424',
		'425',
		'426',
		'427',
		'428',
		'429',
		'430',
		'431',
		'432',
		'433',
		'434',
		'435',
		'436',
		'437',
		'438',
		'439',
		'440',
		'441',
		'442',
		'443',
		'444',
		'445',
		'446',
		'447',
		'448',
		'449',
		'450',
		'451',
		'452',
		'453',
		'454',
		'455',
		'456',
		'457',
		'458',
		'459',
		'460',
		'461',
		'462',
		'463',
		'464',
		'465',
		'466',
		'467',
		'468',
		'469',
		'470',
		'471',
		'472',
		'473',
		'474',
		'475',
		'476',
		'477',
		'478',
		'479',
		'480',
		'481',
		'482',
		'483',
		'484',
		'485',
		'486',
		'487',
		'488',
		'489',
		'490',
		'491',
		'492',
		'493',
		'494',
		'495',
		'496',
		'497',
		'498',
		'499',
		'500',
		'501',
		'502',
		'503',
		'504',
		'505',
		'506',
		'507',
		'508',
		'509',
		'510',
		'511',
		'512',
		'513',
		'514',
		'515',
		'516',
		'517',
		'518',
		'519',
		'520',
		'521',
		'522',
		'523',
		'524',
		'525',
		'526',
		'527',
		'528',
		'529',
		'530',
		'531',
		'532',
		'533',
		'534',
		'535',
		'536',
		'537',
		'538',
		'539',
		'540',
		'541',
		'542',
		'543',
		'544',
		'545',
		'546',
		'547',
		'548',
		'549',
		'550',
		'551',
		'552',
		'553',
		'554',
		'555',
		'556',
		'557',
		'558',
		'559',
		'560',
		'561',
		'562',
		'563',
		'564',
		'565',
		'566',
		'567',
		'568',
		'569',
		'570',
		'571',
		'572',
		'573',
		'574',
		'575',
		'576',
		'577',
		'578',
		'579',
		'580',
		'581',
		'582',
		'583',
		'584',
		'585',
		'586',
		'587',
		'588',
		'589',
		'590',
		'591',
		'592',
		'593',
		'594',
		'595',
		'596',
		'597',
		'598',
		'599',
		'600'])
	redshifts = np.array(['13.8732',
		'13.5321',
		'13.2064',
		'12.8947',
		'12.5966',
		'12.311',
		'12.037',
		'11.7742',
		'11.5218',
		'11.2791',
		'11.0456',
		'10.8209',
		'10.6044',
		'10.3958',
		'10.1943',
		'10.0',
		'9.8197',
		'9.6452',
		'9.4763',
		'9.3125',
		'9.1538',
		'9.0',
		'8.8438',
		'8.6923',
		'8.5454',
		'8.403',
		'8.2647',
		'8.1304',
		'8.0',
		'7.8616',
		'7.7273',
		'7.597',
		'7.4706',
		'7.3478',
		'7.2286',
		'7.1127',
		'7.0',
		'6.8975',
		'6.7975',
		'6.7',
		'6.605',
		'6.5122',
		'6.4217',
		'6.3333',
		'6.2471',
		'6.1628',
		'6.0804',
		'6.0',
		'5.9231',
		'5.8478',
		'5.7742',
		'5.7021',
		'5.6316',
		'5.5625',
		'5.4949',
		'5.4286',
		'5.3636',
		'5.3',
		'5.2376',
		'5.1765',
		'5.1165',
		'5.0577',
		'5.0',
		'4.9434',
		'4.8879',
		'4.8333',
		'4.7798',
		'4.7273',
		'4.6757',
		'4.625',
		'4.5752',
		'4.5263',
		'4.4783',
		'4.431',
		'4.3846',
		'4.339',
		'4.2941',
		'4.25',
		'4.2066',
		'4.1639',
		'4.122',
		'4.0807',
		'4.04',
		'4.0',
		'3.9613',
		'3.9231',
		'3.8855',
		'3.8485',
		'3.812',
		'3.7761',
		'3.7407',
		'3.7059',
		'3.6715',
		'3.6377',
		'3.6043',
		'3.5714',
		'3.539',
		'3.507',
		'3.4755',
		'3.4444',
		'3.4138',
		'3.3836',
		'3.3538',
		'3.3243',
		'3.2953',
		'3.2667',
		'3.2384',
		'3.2105',
		'3.183',
		'3.1558',
		'3.129',
		'3.1026',
		'3.0764',
		'3.0506',
		'3.0252',
		'3.0',
		'2.9745',
		'2.9494',
		'2.9245',
		'2.9',
		'2.8758',
		'2.8519',
		'2.8282',
		'2.8049',
		'2.7818',
		'2.759',
		'2.7365',
		'2.7143',
		'2.6923',
		'2.6706',
		'2.6491',
		'2.6279',
		'2.6069',
		'2.5862',
		'2.5657',
		'2.5455',
		'2.5254',
		'2.5056',
		'2.486',
		'2.4667',
		'2.4475',
		'2.4286',
		'2.4098',
		'2.3913',
		'2.373',
		'2.3548',
		'2.3369',
		'2.3191',
		'2.3016',
		'2.2842',
		'2.267',
		'2.25',
		'2.2332',
		'2.2165',
		'2.2',
		'2.1837',
		'2.1675',
		'2.1515',
		'2.1357',
		'2.12',
		'2.1045',
		'2.0891',
		'2.0739',
		'2.0588',
		'2.0439',
		'2.0291',
		'2.0145',
		'2.0',
		'1.9858',
		'1.9717',
		'1.9577',
		'1.9439',
		'1.9302',
		'1.9167',
		'1.9032',
		'1.8899',
		'1.8767',
		'1.8636',
		'1.8507',
		'1.8378',
		'1.8251',
		'1.8125',
		'1.8',
		'1.7876',
		'1.7753',
		'1.7632',
		'1.7511',
		'1.7391',
		'1.7273',
		'1.7155',
		'1.7039',
		'1.6923',
		'1.6809',
		'1.6695',
		'1.6582',
		'1.6471',
		'1.636',
		'1.625',
		'1.6141',
		'1.6033',
		'1.5926',
		'1.582',
		'1.5714',
		'1.561',
		'1.5506',
		'1.5403',
		'1.5301',
		'1.52',
		'1.51',
		'1.5',
		'1.4901',
		'1.4803',
		'1.4706',
		'1.4609',
		'1.4514',
		'1.4419',
		'1.4324',
		'1.4231',
		'1.4138',
		'1.4046',
		'1.3954',
		'1.3864',
		'1.3774',
		'1.3684',
		'1.3596',
		'1.3507',
		'1.342',
		'1.3333',
		'1.3247',
		'1.3162',
		'1.3077',
		'1.2993',
		'1.2909',
		'1.2826',
		'1.2744',
		'1.2662',
		'1.2581',
		'1.25',
		'1.242',
		'1.234',
		'1.2262',
		'1.2183',
		'1.2105',
		'1.2028',
		'1.1951',
		'1.1875',
		'1.1799',
		'1.1724',
		'1.1649',
		'1.1575',
		'1.1502',
		'1.1429',
		'1.1356',
		'1.1284',
		'1.1212',
		'1.1141',
		'1.107',
		'1.1',
		'1.093',
		'1.0861',
		'1.0792',
		'1.0724',
		'1.0656',
		'1.0588',
		'1.0521',
		'1.0455',
		'1.0388',
		'1.0323',
		'1.0257',
		'1.0192',
		'1.0128',
		'1.0064',
		'1.0',
		'0.9937',
		'0.9873',
		'0.9811',
		'0.9748',
		'0.9687',
		'0.9625',
		'0.9564',
		'0.9503',
		'0.9443',
		'0.9383',
		'0.9323',
		'0.9264',
		'0.9205',
		'0.9146',
		'0.9088',
		'0.903',
		'0.8973',
		'0.8916',
		'0.8859',
		'0.8802',
		'0.8746',
		'0.869',
		'0.8635',
		'0.858',
		'0.8525',
		'0.8471',
		'0.8416',
		'0.8363',
		'0.8309',
		'0.8256',
		'0.8203',
		'0.815',
		'0.8098',
		'0.8046',
		'0.7994',
		'0.7943',
		'0.7892',
		'0.7841',
		'0.779',
		'0.774',
		'0.769',
		'0.764',
		'0.7591',
		'0.7542',
		'0.7493',
		'0.7444',
		'0.7396',
		'0.7348',
		'0.73',
		'0.7253',
		'0.7205',
		'0.7158',
		'0.7112',
		'0.7065',
		'0.7019',
		'0.6973',
		'0.6927',
		'0.6882',
		'0.6836',
		'0.6791',
		'0.6747',
		'0.6702',
		'0.6658',
		'0.6614',
		'0.657',
		'0.6526',
		'0.6483',
		'0.644',
		'0.6397',
		'0.6354',
		'0.6312',
		'0.6269',
		'0.6227',
		'0.6186',
		'0.6144',
		'0.6103',
		'0.6061',
		'0.602',
		'0.598',
		'0.5939',
		'0.5899',
		'0.5859',
		'0.5819',
		'0.5779',
		'0.5739',
		'0.57',
		'0.5661',
		'0.5622',
		'0.5583',
		'0.5545',
		'0.5506',
		'0.5468',
		'0.543',
		'0.5392',
		'0.5355',
		'0.5317',
		'0.528',
		'0.5243',
		'0.5206',
		'0.5169',
		'0.5133',
		'0.5096',
		'0.506',
		'0.5024',
		'0.4988',
		'0.4952',
		'0.4917',
		'0.4882',
		'0.4846',
		'0.4811',
		'0.4776',
		'0.4742',
		'0.4707',
		'0.4673',
		'0.4639',
		'0.4605',
		'0.4571',
		'0.4537',
		'0.4503',
		'0.447',
		'0.4437',
		'0.4404',
		'0.4371',
		'0.4338',
		'0.4305',
		'0.4273',
		'0.424',
		'0.4208',
		'0.4176',
		'0.4144',
		'0.4112',
		'0.4081',
		'0.4049',
		'0.4018',
		'0.3987',
		'0.3956',
		'0.3925',
		'0.3894',
		'0.3863',
		'0.3833',
		'0.3802',
		'0.3772',
		'0.3742',
		'0.3712',
		'0.3682',
		'0.3652',
		'0.3623',
		'0.3593',
		'0.3564',
		'0.3534',
		'0.3505',
		'0.3476',
		'0.3448',
		'0.3419',
		'0.339',
		'0.3362',
		'0.3333',
		'0.3305',
		'0.3277',
		'0.3249',
		'0.3221',
		'0.3193',
		'0.3166',
		'0.3138',
		'0.3111',
		'0.3083',
		'0.3056',
		'0.3029',
		'0.3002',
		'0.2975',
		'0.2948',
		'0.2922',
		'0.2895',
		'0.2869',
		'0.2843',
		'0.2816',
		'0.279',
		'0.2764',
		'0.2738',
		'0.2713',
		'0.2687',
		'0.2661',
		'0.2636',
		'0.261',
		'0.2585',
		'0.256',
		'0.2535',
		'0.251',
		'0.2485',
		'0.246',
		'0.2436',
		'0.2411',
		'0.2387',
		'0.2362',
		'0.2338',
		'0.2314',
		'0.229',
		'0.2266',
		'0.2242',
		'0.2218',
		'0.2194',
		'0.2171',
		'0.2147',
		'0.2124',
		'0.21',
		'0.2077',
		'0.2054',
		'0.2031',
		'0.2008',
		'0.1985',
		'0.1962',
		'0.1939',
		'0.1917',
		'0.1894',
		'0.1871',
		'0.1849',
		'0.1827',
		'0.1805',
		'0.1782',
		'0.176',
		'0.1738',
		'0.1716',
		'0.1695',
		'0.1673',
		'0.1651',
		'0.163',
		'0.1608',
		'0.1587',
		'0.1565',
		'0.1544',
		'0.1523',
		'0.1502',
		'0.1481',
		'0.146',
		'0.1439',
		'0.1418',
		'0.1397',
		'0.1377',
		'0.1356',
		'0.1336',
		'0.1315',
		'0.1295',
		'0.1275',
		'0.1254',
		'0.1234',
		'0.1214',
		'0.1194',
		'0.1174',
		'0.1155',
		'0.1135',
		'0.1115',
		'0.1095',
		'0.1076',
		'0.1056',
		'0.1037',
		'0.1018',
		'0.0998',
		'0.0979',
		'0.096',
		'0.0941',
		'0.0922',
		'0.0903',
		'0.0884',
		'0.0865',
		'0.0846',
		'0.0828',
		'0.0809',
		'0.079',
		'0.0772',
		'0.0753',
		'0.0735',
		'0.0717',
		'0.0698',
		'0.068',
		'0.0662',
		'0.0644',
		'0.0626',
		'0.0608',
		'0.059',
		'0.0572',
		'0.0555',
		'0.0537',
		'0.0519',
		'0.0502',
		'0.0484',
		'0.0467',
		'0.0449',
		'0.0432',
		'0.0415',
		'0.0397',
		'0.038',
		'0.0363',
		'0.0346',
		'0.0329',
		'0.0312',
		'0.0295',
		'0.0278',
		'0.0261',
		'0.0245',
		'0.0228',
		'0.0211',
		'0.0195',
		'0.0178',
		'0.0162',
		'0.0145',
		'0.0129',
		'0.0113',
		'0.0096',
		'0.008',
		'0.0064',
		'0.0048',
		'0.0032',
		'0.0016',
		'0.0014',
		'0.0013',
		'0.0011',
		'0.001',
		'0.0008',
		'0.0006',
		'0.0005',
		'0.0003',
		'0.0002',
		'0.0']).astype(np.float)
	return snapnums[np.where(redshifts == find_nearest(redshifts, z))[0][0]]

class MplColorHelper:
  import numpy as np
  import matplotlib.pyplot as plt
  def __init__(self, cmap_name, start_val, stop_val):
    self.cmap_name = cmap_name
    self.cmap = plt.get_cmap(cmap_name)
    self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
    self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)
  def get_rgb(self, val):
    return self.scalarMap.to_rgba(val)

def getsims(whichsims):
	sims= np.array([]);	labels= np.array([]); host_mvir= np.array([]); host_mstr= np.array([]); colors= np.array([]); 
	rvirs= np.array([]); opcs= np.array([]); zords= np.array([]); linst= np.array([]); linst2= np.array([])

	if whichsims=='all':
		sims        = np.array(['m11q_res880_dmo','m11q_res880'  ,'m11d_res7100','m11e_res7100','m11i_res7100','m11b_res260'])
		labels      = np.array(['m11q DMO'       ,'m11q DM+Hydro','m11d'        ,'m11e'        ,'m11i'        ,'m11b'       ])
		host_mvir   = np.array(['1.8e11'         ,'1.4e11'       , '2.6e11'     ,'1.4e11'      ,'6.7e10'      ,'4.0e10'     ])
		host_mstr   = np.array(['0.0'            ,'3.9e8'        ,'3.9e9'       ,'1.5e9'       ,'1.0e9'       ,'3.0e7'      ])
		colors      = np.array(['black'          ,c.orange       ,c.blue        ,c.green       ,c.purple      ,c.brown      ])
		rvirs       = np.array([116.2            ,106.1          ,131.8         ,107.0         ,83.7          ,70.5         ])
		opcs        = np.array([1.0              ,1.0            ,0.65          ,0.65          ,0.65          ,0.65         ])
		zords       = np.array([275              ,300            ,250           ,100           ,50            ,10           ])
		linst       = np.array(['-'              ,'-'            ,'--'          ,'--'          ,'--'          ,'--'         ])
		linst2      = np.array(['-.'             ,'-.'           ,':'           ,':'           ,':'           ,':'          ])

	else:
		if 'm11q_dmo' in whichsims:
			sims        = np.append(sims     ,'m11q_res880_dmo')
			labels      = np.append(labels   ,'m11q DMO'       )
			host_mvir   = np.append(host_mvir,'1.8e11'         )
			host_mstr   = np.append(host_mstr,'0.0'            )
			colors      = np.append(colors   ,'black'          )
			rvirs       = np.append(rvirs    ,116.2            )
			opcs        = np.append(opcs     ,1.0              )
			zords       = np.append(zords    ,275              )
			linst       = np.append(linst    ,'-'              )
			linst2      = np.append(linst2   ,'-.'             )
		if 'm11q' in whichsims:
			sims        = np.append(sims     ,'m11q_res880'  )
			labels      = np.append(labels   ,'m11q DM+Hydro')
			host_mvir   = np.append(host_mvir,'1.4e11'       )
			host_mstr   = np.append(host_mstr,'3.9e8'        )
			colors      = np.append(colors   ,c.orange       )
			rvirs       = np.append(rvirs    ,106.1          )
			opcs        = np.append(opcs     ,1.0            )
			zords       = np.append(zords    ,300            )
			linst       = np.append(linst    ,'-'            )
			linst2      = np.append(linst2   ,'-.'           )
		if 'm11d' in whichsims:
			sims        = np.append(sims     ,'m11d_res7100')
			labels      = np.append(labels   ,'m11d'        )
			host_mvir   = np.append(host_mvir, '2.6e11'     )
			host_mstr   = np.append(host_mstr,'3.9e9'       )
			colors      = np.append(colors   ,c.blue        )
			rvirs       = np.append(rvirs    ,131.8         )
			opcs        = np.append(opcs     ,0.65          )
			zords       = np.append(zords    ,250           )
			linst       = np.append(linst    ,'--'          )
			linst2      = np.append(linst2   ,':'           )
		if 'm11e' in whichsims:
			sims        = np.append(sims     ,'m11e_res7100')
			labels      = np.append(labels   ,'m11e'        )
			host_mvir   = np.append(host_mvir,'1.4e11'      )
			host_mstr   = np.append(host_mstr,'1.5e9'       )
			colors      = np.append(colors   ,c.green       )
			rvirs       = np.append(rvirs    ,107.0         )
			opcs        = np.append(opcs     ,0.65          )
			zords       = np.append(zords    ,100           )
			linst       = np.append(linst    ,'--'          )
			linst2      = np.append(linst2   ,':'           )
		if 'm11i' in whichsims:
			sims        = np.append(sims     ,'m11i_res7100')
			labels      = np.append(labels   ,'m11i'        )
			host_mvir   = np.append(host_mvir,'6.7e10'      )
			host_mstr   = np.append(host_mstr,'1.0e9'       )
			colors      = np.append(colors   ,c.purple      )
			rvirs       = np.append(rvirs    ,83.7          )
			opcs        = np.append(opcs     ,0.65          )
			zords       = np.append(zords    ,50            )
			linst       = np.append(linst    ,'--'          )
			linst2      = np.append(linst2   ,':'           )
		if 'm11b' in whichsims:
			sims        = np.append(sims     ,'m11b_res260')
			labels      = np.append(labels   ,'m11b'       )
			host_mvir   = np.append(host_mvir,'4.0e10'     )
			host_mstr   = np.append(host_mstr,'3.0e7'      )
			colors      = np.append(colors   ,c.brown      )
			rvirs       = np.append(rvirs    ,70.5         )
			opcs        = np.append(opcs     ,0.65         )
			zords       = np.append(zords    ,10           )
			linst       = np.append(linst    ,'--'         )
			linst2      = np.append(linst2   ,':'          )

	return sims,labels,host_mvir,host_mstr,colors,rvirs,opcs,zords,linst,linst2

def scinote(n,digits=2):

	if n>0:
		return str(np.round(10**(np.log10(n) % 1), digits))+'e'+str(np.int(np.log10(n)))
	else:
		n = np.abs(n)
		return '-'+str(np.round(10**(np.log10(n) % 1), digits))+'e'+str(np.int(np.log10(n)))

def time(scalefactor):
	
	return 2. / (3.*H0G*(np.sqrt(omega_l)))*np.arcsinh( np.sqrt(omega_l/omega_m)*(scalefactor**(1.5)) )

def scalefactor(time):

	return ( np.sqrt(omega_m/omega_l)*np.sinh((3./2.)*H0G*np.sqrt(omega_l)*time)  )**(1./1.5)
