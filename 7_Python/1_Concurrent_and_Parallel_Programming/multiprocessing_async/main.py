import asyncio
import multiprocessing

class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, durations):
        super(MultiprocessingAsync, self).__init__()
        self._durations = durations
    # end

    @staticmethod
    async def async_sleep(duration):
        await asyncio.sleep(duration)
        return duration
    # end

    async def consecutives_sleeps(self):
        pending = set()
        for duration in self._durations:
            pending.add(asyncio.create_task(self.async_sleep(duration)))
        # end

        while len(pending) > 0:
            done, pending = await asyncio.wait(pending, timeout=1)

            for done_task in done:
                print(await done_task)
            # end
        # end
    # end

    def run(self):
        asyncio.run(self.consecutives_sleeps())
        print("Process Finished!!")
    # end



if __name__=="__main__":
    durations = []
    for i in range(1, 11):
        durations.append(i)
    # end

    processes = []
    for i in range(2):
        processes.append(MultiprocessingAsync(durations[i*5:(i+1)*5]))
    # end

    for p in processes:
        p.start()
    # end

    for p in processes:
        p.join()
    # end
