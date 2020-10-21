from django.shortcuts import render

# Create your views here.
def home(request):
	
	import requests

	if request.method=="POST":
		zipcode=request.POST["zipcode"]
		api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=2F799F80-44EF-4438-8A3F-D632F798F44B")
		try:
			#api=json.loads(api_request.content)
			api=api_request.json()
			
		except Exception as e:
			api="Error"

		if api[0]['Category']['Name'] == "Good":
			description="No Risk"
			color="good"
		elif api[0]['Category']['Name'] == "Moderate":
			color="moderate"
			description="Moderate Risk"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			color="usg"
			description="Risky"
		elif api[0]['Category']['Name'] == "Unhealthy":
			color="unhealthy"
			description="Very Risky"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			color="veryunhealthy"
			description="High Risk"
		elif api[0]['Category']['Name'] == "Hazardous":
			color="hazardous"
			description="Do not go outside!"

		return render(request, 'home.html', {'api':api,'description':description,'color':color})

	else:
		api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=2F799F80-44EF-4438-8A3F-D632F798F44B")
		try:
			#api=json.loads(api_request.content)
			api=api_request.json()
		
		
		except Exception as e:
			api="Error"
		if api[0]['Category']['Name'] == "Good":
			description="No Risk"
			color="good"
		elif api[0]['Category']['Name'] == "Moderate":
			color="moderate"
			description="Moderate Risk"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			color="usg"
			description="Risky"
		elif api[0]['Category']['Name'] == "Unhealthy":
			color="unhealthy"
			description="Very Risky"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			color="veryunhealthy"
			description="High Risk"
		elif api[0]['Category']['Name'] == "Hazardous":
			color="hazardous"
			description="Do not go outside!"


		return render(request, 'home.html', {'api':api,'description':description,'color':color})
	

def about(request):
	return render(request, 'about.html', {})