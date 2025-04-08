import os
import psycopg2
from flask import Flask, render_template, request 
from dotenv import load_dotenv

USER_IP_URL = "http://ip-api.com/json/"


user_ip = request.remote_addr
print(user_ip)