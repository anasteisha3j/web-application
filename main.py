import multiprocessing
from website import create_app

def run_app(port):
    app = create_app()
    app.run(debug=False, host="127.0.0.1", port=port)  

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")  
    processes = [
        multiprocessing.Process(target=run_app, args=(5000,)),
        multiprocessing.Process(target=run_app, args=(5001,)),
    ]
    
    for process in processes:
        process.start()

    for process in processes:
        process.join()


