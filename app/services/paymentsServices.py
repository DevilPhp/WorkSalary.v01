from app.database import getDatabase, setDatabase
from app.logger import logger
from app.database.payment import HolidaysPerYear, Holiday

class PaymentServices:

    @staticmethod
    def getHolidaysForYear(selectedYear):
        with getDatabase() as session:
            returnedData = []
            year = session.query(HolidaysPerYear).filter_by(Year=selectedYear).first()
            if year:
                holidays = session.query(Holiday).filter_by(HolidaysPerYearId=year.id).all()
                for holiday in holidays:
                    returnedData.append({'name': holiday.HolidayName, 'date': holiday.HolidayDate})
            return returnedData

    @staticmethod
    def addHoliday(name, date, user, selectedYear):
        with setDatabase() as session:
            year = session.query(HolidaysPerYear).filter_by(Year=selectedYear).first()
            newHoliday = Holiday(HolidayName=name, HolidayDate=date, UpdatedBy=user, HolidaysPerYearId=year.id)
            session.add(newHoliday)
            year.HolidaysCount += 1
            session.commit()
            logger.info(f'Added new holiday: {name} on {date} by {user}')

    @staticmethod
    def getHolidaysYears():
        # returnedYears = []
        with getDatabase() as session:
            years = session.query(HolidaysPerYear.Year).order_by(HolidaysPerYear.Year).all()
            returnedYears = [year[0] for year in years]
            return returnedYears

    @staticmethod
    def addHolidaysYear(year, user):
        with setDatabase() as session:
            newHolidaysYear = HolidaysPerYear(Year=year, HolidaysCount=0, UpdatedBy=user)
            session.add(newHolidaysYear)
            session.commit()
            logger.info(f'Added new holidays year: {year} by {user}')
