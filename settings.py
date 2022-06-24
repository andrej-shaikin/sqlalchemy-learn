from environ import Env

env = Env()
Env.read_env()

DATABASE_DSN = env.str("DATABASE_DSN")

