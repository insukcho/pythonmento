### IDLE 에서 <Ctrl> + <N> 키를 눌러서 새창에서 작업하세요!! ###

# 로깅 모듈 탑재
import logging

# 콘솔 출력용 핸들러 생성
handler = logging.StreamHandler()

# 포매터 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')

# 핸들러에 포매터 설정
handler.setFormatter(formatter)

# 로거 생성 및 로그 레벨 설정
logger = logging.getLogger(__name__)            # 로거 생성
logger.setLevel(logging.INFO)                   # 로그 레벨설정 : INFO
logger.addHandler(handler)                      # 해당 로거에 핸들러 추가

# 로그 메시지 출력
logger.debug('이 메시지는 개발자만 이해해요.')	# DEBUG 로그 출력
logger.info('생각대로 동작 하고 있어요.')	        # INFO 로그 출력
logger.warn('곧 문제가 생길 가능성이 높습니다.')	# WARNING 로그 출력
logger.error('문제가 생겼어요.기능이 동작 안해요.')	# ERROR 로그 출력
logger.critical('시스템이 다운됩니다!!!!')	        # CRITICAL 로그 출력
