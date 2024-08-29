from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def attend_meeting(self):
        pass

    @abstractmethod
    def submit_report(self):
        pass


class Manager(Worker):
    def work(self):
        return "Manager is working on a project."

    def attend_meeting(self):
        return "Manager is attending a meeting."

    def submit_report(self):
        return "Manager is submitting a report."


class Developer(Worker):
    def work(self):
        return "Developer is writing code."

    def attend_meeting(self):
        return "Developer is attending a meeting."

    def submit_report(self):
        return "Developer is submitting a report."


class Intern(Worker):
    def work(self):
        return "Intern is doing tasks."

    def attend_meeting(self):
        return "Intern is attending a meeting."

    def submit_report(self):
        # Interns don't submit reports
        raise NotImplementedError("Interns don't submit reports.")


# Function that processes worker tasks
def process_worker(worker: Worker):
    print(worker.work())
    print(worker.attend_meeting())
    print(worker.submit_report())


# Now let's test it
manager = Manager()
developer = Developer()
intern = Intern()

process_worker(manager)
process_worker(developer)
process_worker(intern)  # This will raise an exception because Intern doesn't implement submit_report()

"""
- We've split the Worker interface into three smaller, more specific interfaces: Workable, MeetingAttendee, and Reportable.
- Manager and Developer implement all three interfaces because they need to work, attend meetings, and submit reports.
- Intern only implements Workable and MeetingAttendee because interns do not need to submit reports.
- This design adheres to the Interface Segregation Principle by ensuring that classes only implement the interfaces they need.

"""



from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class MeetingAttendee(ABC):
    @abstractmethod
    def attend_meeting(self):
        pass


class Reportable(ABC):
    @abstractmethod
    def submit_report(self):
        pass


class Manager(Workable, MeetingAttendee, Reportable):
    def work(self):
        return "Manager is working on a project."

    def attend_meeting(self):
        return "Manager is attending a meeting."

    def submit_report(self):
        return "Manager is submitting a report."


class Developer(Workable, MeetingAttendee, Reportable):
    def work(self):
        return "Developer is writing code."

    def attend_meeting(self):
        return "Developer is attending a meeting."

    def submit_report(self):
        return "Developer is submitting a report."


class Intern(Workable, MeetingAttendee):
    def work(self):
        return "Intern is doing tasks."

    def attend_meeting(self):
        return "Intern is attending a meeting."


# Function that processes worker tasks
def process_work(worker: Workable):
    print(worker.work())


def process_meeting(attendee: MeetingAttendee):
    print(attendee.attend_meeting())


def process_report(reportable: Reportable):
    print(reportable.submit_report())


# Now let's test it
manager = Manager()
developer = Developer()
intern = Intern()

process_work(manager)
process_meeting(manager)
process_report(manager)

process_work(developer)
process_meeting(developer)
process_report(developer)

process_work(intern)
process_meeting(intern)
# process_report(intern)  # This won't work because Intern doesn't implement Reportable
