from app.database import getDatabase, setDatabase
from app.logger import logger
from app.database.payment import HolidaysPerYear, Holiday, PaymentPerMinute, NightPaymentPerMinute

class PaymentServices:

    @staticmethod
    def getPayPerMin(dayMin=True):
        with getDatabase() as session:
            returnedData = []
            if dayMin:
                payPerMins = session.query(PaymentPerMinute).all()
            else:
                payPerMins = session.query(NightPaymentPerMinute).all()
            for payPerMin in payPerMins:
                returnedData.append({'id': payPerMin.id,
                                     'valueLeva': payPerMin.PaymentValue if dayMin else payPerMin.NightPaymentValue,
                                     'valueEUR': payPerMin.PaymentInEuro if dayMin else payPerMin.NightPaymentInEuro,
                                     'dateActive': payPerMin.DateActive,
                                     'comment': payPerMin.Comment,
                                     'lastUpdated': payPerMin.LastUpdated,
                                     'updatedBy': payPerMin.UpdatedBy})
            return returnedData

    # @staticmethod
    # def getPayPerMinNight():
    #     with getDatabase() as session:
    #         returnedData = []
    #         payPerNightMins = session.query(NightPaymentPerMinute).all()
    #         for payPerMin in payPerNightMins:
    #             returnedData.append({'id': payPerMin.id,
    #                                  'valueLeva': payPerMin.NightPaymentValue,
    #                                  'valueEUR': payPerMin.NightPaymentInEuro,
    #                                  'dateActive': payPerMin.DateActive,
    #                                  'comment': payPerMin.Comment,
    #                                  'lastUpdated': payPerMin.LastUpdated,
    #                                  'updatedBy': payPerMin.UpdatedBy})
    #         return returnedData

    @staticmethod
    def getHolidaysForYear(selectedYear):
        with getDatabase() as session:
            returnedData = []
            year = session.query(HolidaysPerYear).filter_by(Year=selectedYear).first()
            if year:
                holidays = session.query(Holiday).filter_by(HolidaysPerYearId=year.id).all()
                for holiday in holidays:
                    returnedData.append({'id': holiday.id, 'name': holiday.HolidayName, 'date': holiday.HolidayDate})
            print(returnedData)
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
    def deleteHoliday(holidayId, year, user):
        with setDatabase() as session:
            holiday = session.query(Holiday).filter_by(id=holidayId).first()
            if holiday:
                year = session.query(HolidaysPerYear).filter_by(Year=year).first()
                session.delete(holiday)
                year.HolidaysCount -= 1
                session.commit()
                logger.info(f'Deleted holiday: {holiday.HolidayName} on {holiday.HolidayDate} by {user}')
                return True

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
