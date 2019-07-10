from locust import HttpLocust, TaskSet, task


class Test_1(TaskSet):

    @task(2)
    def users(self):
        self.client.get("users")

    @task(1)
    def photos(self):
        self.client.get("photos")


class UserBahavior_1(HttpLocust):
    task_set = Test_1
    min_wait = 5000
    max_wait = 9000


class Test_2(TaskSet):

    @task(2)
    def comments(self):
        self.client.get("comments")

    @task(1)
    def todos(self):
        self.client.get("todos")


class UserBahavior_2(HttpLocust):
    task_set = Test_2
    min_wait = 2000
    max_wait = 3000