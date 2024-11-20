import threading
import time
import queue

# 메시지 클래스
class Message:
    def __init__(self, sender_name, file_path, param1, param2):
        self.sender_name = sender_name
        self.file_path = file_path
        self.param1 = param1
        self.param2 = param2

# 워커 스레드 클래스
class WorkerThread(threading.Thread):
    def __init__(self, name, message_queue, stop_event):
        super().__init__()
        self.name = name
        self.message_queue = message_queue
        self.stop_event = stop_event  # 종료를 위한 이벤트 플래그

    def run(self):
        while not self.stop_event.is_set():
            time.sleep(3)
            message = Message(
                sender_name=self.name,
                file_path=f"/path/to/file_from_{self.name}.txt",
                param1=f"param1_from_{self.name}",
                param2=f"param2_from_{self.name}",
            )
            self.message_queue.put(message)

# 메인 스레드에서 메시지 처리 함수
def handle_message(message):
    print(f"[Message Received]")
    print(f"Sender: {message.sender_name}")
    print(f"File Path: {message.file_path}")
    print(f"Param1: {message.param1}")
    print(f"Param2: {message.param2}")
    print("-" * 40)

# 메인 실행
if __name__ == "__main__":
    stop_event = threading.Event()  # 종료 제어를 위한 이벤트
    message_queue = queue.Queue()
    workers = [WorkerThread(name=f"Worker-{i+1}", message_queue=message_queue, stop_event=stop_event) for i in range(2)]

    for worker in workers:
        worker.start()

    try:
        while not stop_event.is_set():
            # 큐에서 메시지를 블로킹 모드로 가져오기 (타임아웃으로 종료 시도 처리)
            try:
                print("메시지 대기 중...")
                message = message_queue.get(timeout=1)  # 1초 타임아웃
                handle_message(message)
            except queue.Empty:
                # 큐가 비어 있는 경우 아무것도 하지 않음
                pass
    except KeyboardInterrupt:
        print("종료 중...")
        stop_event.set()  # 종료 신호 설정
        for worker in workers:
            worker.join()  # 워커 스레드 종료 대기
        print("모든 워커 스레드가 종료되었습니다.")
