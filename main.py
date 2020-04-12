import logging, os, sys, requests, uuid
from bs4 import BeautifulSoup
from models import Models
from peewee import *
from dotenv import load_dotenv

def main():

	urlRequest = os.getenv('URL_SESA')
	logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
	pageRequest = requests.get(urlRequest)
	treeDom = BeautifulSoup(pageRequest.content, 'html.parser')

	negative = treeDom.select('div.container-fluid div.card-deck div.card.mb-4.border-success.text-center div.card-body h5.display-4')[0].text
	analyzing = treeDom.select('div.container-fluid div.card-deck div.card.mb-4.border-warning.text-center div.card-body h5.display-4')[0].text
	positives = treeDom.select('div.container-fluid div.card-deck div.card.mb-4.border-danger.text-center div.card-body h5.display-4')[0].text
	deaths = treeDom.select('div.container-fluid div.card-deck div.card.mb-4.border-dark.text-center div.card-body h5.display-4')[0].text
	recovered = treeDom.select('div.container-fluid div.card-deck div.card.mb-4.border-primary.text-center div.card-body h5.display-4')[0].text
	dateString = treeDom.select('div.container-fluid h3.text-center')[0].text

	logging.info('Negative cases {}'.format(negative))
	logging.info('Analyzing cases {}'.format(analyzing))
	logging.info('Positives cases {}'.format(positives))
	logging.info('Death cases {}'.format(deaths))
	logging.info('Recovered cases {}'.format(recovered))

	Models.create_tables()
	query = Models.GeneralCase.select().where(Models.GeneralCase.uuid == uuid.uuid5(uuid.NAMESPACE_OID,dateString))
	if not query.count():
		logging.info('Found new case, updating database.')
		Models.GeneralCase.create(uuid = uuid.uuid5(uuid.NAMESPACE_OID,dateString), negative = negative, analyzing = analyzing, positives = positives, deaths = deaths, recovered = recovered)

if __name__ == '__main__':
	load_dotenv()
	main()
