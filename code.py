import uuid
# uniq id : uuid.uuid4()
from abc import ABC,abstractmethod
import random as rd

def uniq_id(length):
    chars=[chr(m) for m in range(41,127)]*length
    rd.shuffle(chars)
    return ''.join(chars)[:length]

class Multinational:
    def __init__(self,name,country):
        self.__name=name
        self.__country=country
        self.__subsidiaries=[]

    def addSubsidiary(self,subsidiary):
        self.__subsidiaries.append(subsidiary)

    def changeLocationOfEmployment(self,employee,location):
        if location in self.__subsidiaries:
            actual_location=None
            for subsidiary in self.__subsidiaries:
                if employee in subsidiary.getEmployees():
                    actual_location=subsidiary
                    break
            if actual_location is not None:
                actual_location.removeEmployee(employee)
                location.addEmployee(employee)

    def getInformation(self):
        print('- La multinationale '+self.__name+' est composée de '+str(len(self.__subsidiaries))+' filiale'+('s' if len(self.__subsidiaries)>1 else '')+". Son pays d'origine est "+self.__country+'.')
        oldest_subsidiary=sorted(self.__subsidiaries,key=lambda k:k.getCreationDate())[0]
        print('- La filiale la plus ancienne de cette multinationale est : '+str(oldest_subsidiary.getName())+'. Elle est composée de '+str(len(oldest_subsidiary.getEmployees()))+' salarié'+('s' if len(oldest_subsidiary.getEmployees())>1 else '')+'.')
        employees=[]
        for subsidiary in self.__subsidiaries:
            employees.extend(subsidiary.getEmployees())
        print('- '+self.__name+' est composée de '+str(len(employees))+' salarié'+('s' if len(employees)>1 else '')+' :')
        for employee in employees:
            location=None
            for subsidiary in self.__subsidiaries:
                if employee in subsidiary.getEmployees():
                    location=subsidiary
                    break
            print('* '+employee.getInformation()+(', Site : '+str(location.getCountry()) if location is not None else ''))

class Subsidiary:
    def __init__(self, name, country, creation_date):
        self.__name = name
        self.__country = country
        self.__creation_date = creation_date
        self.__employees = []

    def addEmployee(self,employee):
        self.__employees.append(employee)

    def removeEmployee(self,employee):
        if self.__employees.index(employee)!=-1:
            del self.__employees[self.__employees.index(employee)]

    def getEmployees(self):
        return self.__employees

    def getName(self):
        return self.__name

    def getCreationDate(self):
        return self.__creation_date

    def getCountry(self):
        return self.__country

class Salaryman(ABC):
    def __init__(self,lastname,firstname,salary_level):
        self._lastname = lastname
        self._firstname = firstname
        self._salary_level = salary_level
        self._id = uniq_id(20)

    @abstractmethod
    def getInformation(self):
        pass

class Director(Salaryman):
    def __init__(self, lastname, firstname, salary_level, appointment_year):
        Salaryman.__init__(self, lastname, firstname, salary_level)
        self._appointment_year = appointment_year
        self._status='Directeur'

    def getInformation(self):
        return "[id=" + str(self._id) + "] Nom et Prénom : " + self._lastname + ' ' + self._firstname + ', Salaire : ' + str(self._salary_level) + ', Statut : ' + self._status + ", Année de nomination : " + str(self._appointment_year)


class Employee(Salaryman,ABC):
    def __init__(self, lastname, firstname, salary_level, hire_year, work_days):
        Salaryman.__init__(self, lastname, firstname, salary_level)
        self._hire_year=hire_year
        self._work_days=work_days

    @abstractmethod
    def getInformation(self):
        pass

class Administrative(Employee):
    def __init__(self, lastname, firstname, salary_level, hire_year, work_days, service):
        Employee.__init__(self, lastname, firstname, salary_level, hire_year, work_days)
        self._service = service
        self._status='Administratif'

    def getInformation(self):
        return "[id=" + str(self._id) + "] Nom et Prénom : " + self._lastname + ' ' + self._firstname + ', Salaire : ' + str(self._salary_level) + ', Statut : ' + self._status + ", Année d'embauche : " + str(self._hire_year)+", Jours travaillés : " + str(self._work_days) + ", Service : " + self._service

class Engineer(Employee,ABC):
    def __init__(self,lastname, firstname, salary_level, hire_year, work_days, project_hours, managment_hours):
        Employee.__init__(self, lastname, firstname, salary_level, hire_year, work_days)
        self._project_hours=project_hours
        self._managment_hours=managment_hours

    @abstractmethod
    def getInformation(self):
        pass

class Junior_Engineer(Engineer):
    def __init__(self,lastname, firstname, salary_level, hire_year, work_days, project_hours, managment_hours, years_experience):
        Engineer.__init__(self,lastname, firstname, salary_level, hire_year, work_days, project_hours, managment_hours)
        self._years_experience=years_experience
        self._status='Ingénieur-junior'

    def getInformation(self):
        return "[id=" + str(self._id) + "] Nom et Prénom : " + self._lastname + ' ' + self._firstname + ', Salaire : ' + str(self._salary_level) + ', Statut : ' + self._status + ", Année d'embauche : " + str(self._hire_year) + ", Jours travaillés : " + str(self._work_days) + ", Nombre d'heures de projet : " + str(self._project_hours)+ ", Nombre d'heures de gestion : " + str(self._managment_hours)+ ", Nombre d'heures de gestion : " + str(self._managment_hours)+ ", Nombre d'années d'expérience : " + str(self._years_experience)

class Senior_Engineer(Engineer):
    def __init__(self, lastname, firstname, salary_level, hire_year, work_days, project_hours, managment_hours,responsability):
        Engineer.__init__(self, lastname, firstname, salary_level, hire_year, work_days, project_hours, managment_hours)
        self._responsability = responsability
        self._status = 'Ingénieur-senior'

    def getInformation(self):
        return "[id=" + str(self._id) + "] Nom et Prénom : " + self._lastname + ' ' + self._firstname + ', Salaire : ' + str(self._salary_level) + ', Statut : ' + self._status + ", Année d'embauche : " + str(self._hire_year) + ", Jours travaillés : " + str(self._work_days) + ", Nombre d'heures de projet : " + str(self._project_hours)+ ", Nombre d'heures de gestion : " + str(self._managment_hours)+ ", Nombre d'heures de gestion : " + str(self._managment_hours)+ ", Responsabilté : " + str(self._responsability)


# Q° 3-a
multinational=Multinational(name='RCAT',country='la France')

# Q° 3-b
subsidiary1=Subsidiary(name='RCAT-Belgique',country='Belgique',creation_date=2005)
subsidiary2=Subsidiary(name='RCAT-Maroc',country='Maroc',creation_date=2008)
subsidiary3=Subsidiary(name='RCAT-Tunisie',country='Tunisie',creation_date=2002)
subsidiary4=Subsidiary(name='RCAT-Angleterre',country='Angleterre',creation_date=2015)
subsidiaries=[subsidiary1,subsidiary2,subsidiary3,subsidiary4]
for subsidiary in subsidiaries:
    multinational.addSubsidiary(subsidiary)

# Q° 3-c
director=Director(lastname='Nom0',firstname='Prenom0',salary_level=6,appointment_year=2008)
subsidiary3.addEmployee(director)

# Q° 3-d-i
administrative3=Administrative(lastname='Nom1',firstname='Prenom1',salary_level=2,hire_year=2019,work_days=253,service='RH')
seniorEngineer3=Senior_Engineer(lastname='Nom2',firstname='Prenom2',salary_level=3,hire_year=2018,work_days=253,project_hours=300,managment_hours=300,responsability="Chef de l'équipe data science")
subsidiary3.addEmployee(administrative3)
subsidiary3.addEmployee(seniorEngineer3)

# Q° 3-d-ii
administrative1=Administrative(lastname='Nom3',firstname='Prenom3',salary_level=1,hire_year=2017,work_days=253,service='Comptabilité')
juniorEngineer1=Junior_Engineer(lastname='Nom4',firstname='Prenom4',salary_level=2,hire_year=2020,work_days=250,project_hours=300,managment_hours=303,years_experience=2)
subsidiary1.addEmployee(administrative1)
subsidiary1.addEmployee(juniorEngineer1)

# Q° 3-d-iii
seniorEngineer2=Senior_Engineer(lastname='Nom5',firstname='Prenom5',salary_level=2,hire_year=2015,work_days=253,project_hours=300,managment_hours=300,responsability="Chef de l'équipe développement web")
subsidiary2.addEmployee(seniorEngineer2)

# Q° 3-e
multinational.getInformation()

# Q° 3-f
subsidiary3.removeEmployee(administrative3)

# Q° 3-g
print('-----')
multinational.getInformation()

# Q° 3-h
multinational.changeLocationOfEmployment(seniorEngineer3,subsidiary1)

# Q° 3-i
print('-----')
multinational.getInformation()