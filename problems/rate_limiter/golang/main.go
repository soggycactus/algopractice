package main

type Logger struct {
	messages map[string]int
}

func Constructor() Logger {
	return Logger{
		messages: make(map[string]int),
	}
}

func (this *Logger) ShouldPrintMessage(timestamp int, message string) bool {
	if lookup, ok := this.messages[message]; ok {
		if (timestamp - lookup) >= 10 {
			this.messages[message] = timestamp
			return true
		}
		return false
	}

	this.messages[message] = timestamp
	return true
}

func main() {
	logger := Constructor()
	println(logger.ShouldPrintMessage(1, "foo"))
	println(logger.ShouldPrintMessage(2, "bar"))
	println(logger.ShouldPrintMessage(3, "foo"))
	println(logger.ShouldPrintMessage(8, "bar"))
	println(logger.ShouldPrintMessage(10, "foo"))
	println(logger.ShouldPrintMessage(11, "foo"))
	println(logger.ShouldPrintMessage(12, "foo"))
}

/**
 * Your Logger object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.ShouldPrintMessage(timestamp,message);
 */
