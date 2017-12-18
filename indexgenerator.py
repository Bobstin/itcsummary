import pdb
import os
import django
import pandas as pd
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ITC2017Summary.settings")
django.setup()
from contentsummary.models import Speaker, Company, Speech

index = []
for company in Company.objects.all():
	speakers = Speaker.objects.filter(company=company)
	for speaker in speakers:
		speechs = Speech.objects.filter(speaker=speaker)
		for speech in speechs:
			index.append({
				'Company':company.name,
				'Speaker':speaker.name,
				'Session': speech.session.name,
				'Number':speech.session.number
				})
		
index_df = pd.DataFrame(index)
index_df = index_df[['Company','Speaker','Session','Number']]
writer = pd.ExcelWriter('{} Generated index.xlsx'.format(time.strftime('%Y%m%d %H%M',time.localtime())), engine = 'xlsxwriter')
index_df.to_excel(writer,sheet_name='Index',index=False)
writer.close()



