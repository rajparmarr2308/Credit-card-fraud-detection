import io
import pickle
import pandas as pd
from django.shortcuts import render,redirect,get_object_or_404
from django.http.response import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import DataFileUpload

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score


def base(request):
    return render(request,'homeApp/landing_page.html')
    
def upload_credit_data(request):
    return render(request,'homeApp/upload_credit_data.html')

def prediction_button(request,id):
    return render(request,'homeApp/fraud_detection.html', {'id': id})
    
def reports(request):
    all_data_files_objs=DataFileUpload.objects.all()
    return render(request,'homeApp/reports.html',{'all_files':all_data_files_objs})
    
def enter_form_data_manually(request):
    return render(request,'homeApp/enter_form_data_manually.html')

def predict_data_manually(request):
    return render(request,'homeApp/predict_data_manually.html')

def add_files_single(request, id):
    return render(request,'homeApp/add_files_single.html', {'id': id})

def predict_csv_single(request,id):
    if request.method == 'POST':
        try:
            obj = DataFileUpload.objects.get(id=id)

            # Deserialize the stored model
            model_binary = obj.trained_model_data
            loaded_model = pickle.loads(model_binary)

             # Deserialize X_test and y_test
            X_test = pickle.loads(obj.x_test_data)
            y_test = pickle.loads(obj.y_test_data)

            # Predict on X_test
            y_pred = loaded_model.predict(X_test)

            # Calculate precision
            precision = precision_score(y_test, y_pred)

            dataFrame = pd.read_csv(request.FILES['actual_file_name'])
            prediction = loaded_model.predict(dataFrame)
            

            status = "Non-Fraudulent Transaction"
            if prediction[0] == 1:
                status = "Fraudulent Transaction"

            context = {
                'status': status,
                'precision': f'{precision:.2%}',  # display it as a percentage
                'data': dataFrame.iloc[0]
            }
        
            return render(request,'homeApp/predict_csv_single.html', context)
                
        except:
            messages.warning(request, "Invalid/wrong format. Please upload File.")
            return  redirect(f'/add_files_single/{id}')

def add_files_multi(request, id):
    return render(request,'homeApp/add_files_multi.html', {'id': id})
    
def predict_csv_multi(request, id):
    if request.method == 'POST':
        try:
            obj = DataFileUpload.objects.get(id=id)

            # Deserialize the stored model
            model_binary = obj.trained_model_data
            loaded_model = pickle.loads(model_binary)

             # Deserialize X_test and y_test
            X_test = pickle.loads(obj.x_test_data)
            y_test = pickle.loads(obj.y_test_data)

            # Predict on X_test
            y_pred = loaded_model.predict(X_test)

            # Calculate precision
            precision = precision_score(y_test, y_pred)

            dataFrame = pd.read_csv(request.FILES['actual_file_name'])
            predictions = loaded_model.predict(dataFrame)

            statuses = ["Fraudulent Transaction" if pred == 1 else "Non-Fraudulent Transaction" for pred in predictions]

            combined_data = []
            for record, status in zip(dataFrame.to_dict(orient='records'), statuses):
                combined_data.append({
                    'record': record,
                    'status': status
                })
            context = {
                'precision': f'{precision:.2%}',    # Precision as a percentage
                'combined_data': combined_data,
            }
        
            return render(request,'homeApp/predict_csv_multi.html', context)
                
        except:
            messages.warning(request, "Invalid/wrong format. Please upload File.")
            return  redirect(f'/add_files_multi/{id}')

def account_details(request):
    return render(request,'homeApp/account_details.html')
def change_password(request):
    return render(request,'homeApp/change_password.html')
def analysis(request,id):
    obj = DataFileUpload.objects.get(id=id)
    df = pd.read_csv(obj.actual_file.path)

    # Empty DataFrame Columns
    empty_columns = len(df.columns[df.isnull().all()].tolist())

    # Data Shape
    data_shape = df.shape

    # Unique Target Values
    # Assuming 'Class' is your target column
    unique_targets = df['Class'].unique().tolist()

    # Percentages
    percent_no_problem = 100 * (df[df['Class'] == 0].shape[0] / df.shape[0])
    percent_problem = 100 * (df[df['Class'] == 1].shape[0] / df.shape[0])

    # Null values check
    has_null = df.isnull().any().any()

    # Transactions
    fraud_transactions = df[df['Class'] == 1]
    normal_transactions = df[df['Class'] == 0]

    fraud_shape = fraud_transactions.shape
    normal_shape = normal_transactions.shape

    # Return or pass these to your template as context
    context = {
        'data_shape': data_shape,
        'unique_targets': unique_targets,
        'percent_no_problem': round(percent_no_problem, 3),
        'percent_problem': round(percent_problem, 3),
        'has_null': has_null,
        'fraud_shape': fraud_shape,
        'normal_shape': normal_shape
    }

    return render(request,'homeApp/analysis.html', context)
def view_data(request,id):
    obj = DataFileUpload.objects.get(id=id)
    df = pd.read_csv(obj.actual_file.path)
    columns = df.columns.tolist()
    return render(request,'homeApp/view_data.html', {'id': id, 'columns': columns})
def delete_data(request,id):
    obj=DataFileUpload.objects.get(id=id)
    obj.delete()
    messages.success(request, "File Deleted succesfully",extra_tags = 'alert alert-success alert-dismissible show')
    return HttpResponseRedirect('/reports')
def upload_data(request):
    if request.method == 'POST':
            data_file_name  = request.POST.get('data_file_name')
            try:
                actual_file = request.FILES['actual_file_name']
                data = pd.read_csv(actual_file)
                
                # Assuming last column is the target variable and others are features
                X = data.iloc[:, :-1].values
                y = data.iloc[:, -1].values
                
                # Splitting the dataset into training and test sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
                
                # Feature scaling
                sc = StandardScaler()
                X_train = sc.fit_transform(X_train)
                X_test = sc.transform(X_test)
                
                # Train the logistic regression model
                classifier = LogisticRegression(random_state=0)
                classifier.fit(X_train, y_train)
                
                # Serialize the model
                serialized_model = pickle.dumps(classifier)
                serialized_x_test = pickle.dumps(X_test)
                serialized_y_test = pickle.dumps(y_test)
                
                description  = request.POST.get('description')

                DataFileUpload.objects.create(
                        file_name=data_file_name,
                        actual_file=actual_file,
                        description=description,
                        trained_model_data=serialized_model,
                        x_test_data=serialized_x_test,
                        y_test_data=serialized_y_test
                    )
                
                
                messages.success(request, "File Uploaded succesfully",extra_tags = 'alert alert-success alert-dismissible show')
                return HttpResponseRedirect('/reports')
                
            except:
                messages.warning(request, "Invalid/wrong format. Please upload File.")
                return redirect('/upload_credit_data')
            

def retrieve_data_by_id(request, id):
    obj = DataFileUpload.objects.get(id=id)
    df = pd.read_csv(obj.actual_file.path)

    # Receive parameters from DataTables on the frontend
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    
    # Paginate the data from the CSV using start and length
    paginated_df = df.iloc[start:start+length].reset_index()
    paginated_df['index'] = paginated_df['index'] + 1 + start

    # Convert the paginated data to a list of lists
    data = paginated_df.values.tolist()

    # Return a JSON response suitable for DataTables
    return JsonResponse({
        'draw': draw,
        'recordsTotal': len(df),
        'recordsFiltered': len(df),  # In case you add server-side filtering later on
        'data': data,
    })

def userLogout(request):
    try:
      del request.session['username']
    except:
      pass
    logout(request)
    return HttpResponseRedirect('/') 
    

def login2(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        
        else:    
            data['error'] = "Username or Password is incorrect"
            res = render(request, 'homeApp/login.html', data)
            return res
    else:
        return render(request, 'homeApp/login.html', data)


def about(request):
    return render(request,'homeApp/about.html')

def dashboard(request):
    return render(request,'homeApp/dashboard.html')
