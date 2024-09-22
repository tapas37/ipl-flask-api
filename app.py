from flask import Flask,jsonify,request
import ipl
ball_withmatch=ipl.ball_withmatch


app=Flask(__name__)

@app.route('/')
def home():
    return "TAPAS"

@app.route('/api/teams')
def teams():
    teams=ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')

    response=ipl.teamVteamAPI(team1,team2)

    print(response)


    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name=request.args.get('team')
    response=ipl.allRecord(team_name)
    return jsonify(response)


@app.route('/api/batsman-record')
def batsman_record():
    batsman_name=request.args.get('batsman')

    response=ipl.batsmanRecord(batsman_name,ball_withmatch)
    return jsonify(response)


@app.route('/api/batsmen')
def batsmen():
    batsmen = ipl.allBatsmen()
    return jsonify(batsmen)




app.run(debug=True)