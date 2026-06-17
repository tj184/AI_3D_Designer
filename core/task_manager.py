"""
Task Manager

Runs long operations in background threads.

Examples

AI Generation
CAD Generation
Export STL
Export STEP
Autosave

Uses ThreadPoolExecutor instead of raw threads.
"""

from concurrent.futures import ThreadPoolExecutor
import traceback
import uuid

from core.event_bus import event_bus


class TaskManager:

    ##########################################################

    def __init__(self, max_workers=4):

        self.executor = ThreadPoolExecutor(
            max_workers=max_workers,
            thread_name_prefix="AI3DWorker"
        )

        self.tasks = {}

    ##########################################################

    def submit(
        self,
        task_name,
        func,
        *args,
        callback=None,
        error_callback=None,
        **kwargs
    ):
        """
        Submit a background task.

        Example

        task_manager.submit(
            "Generate CAD",
            cad.generate,
            code
        )
        """

        task_id = str(uuid.uuid4())

        future = self.executor.submit(
            func,
            *args,
            **kwargs
        )

        self.tasks[task_id] = {

            "id": task_id,

            "name": task_name,

            "future": future

        }

        event_bus.publish(
            "TASK_STARTED",
            {
                "id": task_id,
                "name": task_name
            }
        )

        future.add_done_callback(

            lambda f: self._task_finished(

                task_id,

                future,

                callback,

                error_callback

            )

        )

        return task_id

    ##########################################################

    def _task_finished(

        self,

        task_id,

        future,

        callback,

        error_callback

    ):

        info = self.tasks.get(task_id)

        if info is None:

            return

        try:

            result = future.result()

            event_bus.publish(

                "TASK_COMPLETED",

                {

                    "id": task_id,

                    "name": info["name"],

                    "result": result

                }

            )

            if callback:

                callback(result)

        except Exception as ex:

            traceback.print_exc()

            event_bus.publish(

                "TASK_FAILED",

                {

                    "id": task_id,

                    "name": info["name"],

                    "error": str(ex)

                }

            )

            if error_callback:

                error_callback(ex)

        finally:

            if task_id in self.tasks:

                del self.tasks[task_id]

    ##########################################################

    def active_tasks(self):

        """
        Returns currently running tasks.
        """

        return len(self.tasks)

    ##########################################################

    def shutdown(self):

        """
        Shutdown thread pool.
        """

        self.executor.shutdown(wait=False)

    ##########################################################

    def cancel_all(self):

        """
        Cancel tasks that have not started.
        """

        for task in self.tasks.values():

            task["future"].cancel()

        self.tasks.clear()