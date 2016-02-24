import logging					# 로깅 모듈 탑재
import logging.config                           # 로깅 설정 모듈 탑재
 
# 설정 파일 읽어 오기
logging.config.fileConfig('12-2.logging.conf')

# 로거 생성
logger = logging.getLogger(__name__)            # 로거 생성

# 로그 메시지 출력
logger.debug('이 메시지는 개발자만 이해해요.')	# DEBUG 로그 출력
logger.info('생각대로 동작 하고 있어요.')	        # INFO 로그 출력
logger.warn('곧 문제가 생길 가능성이 높습니다.')	# WARNING 로그 출력
logger.error('문제가 생겼어요.기능이 동작 안해요.')	# ERROR 로그 출력
logger.critical('시스템이 다운됩니다!!!!')	        # CRITICAL 로그 출력
