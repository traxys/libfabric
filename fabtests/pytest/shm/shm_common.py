def shm_run_client_server_test(cmdline_args, executable, iteration_type,
                               completion_semantic, memory_type,
                               warmup_iteration_type=None):
    from common import ClientServerTest

    test = ClientServerTest(cmdline_args, executable, iteration_type,
                            completion_semantic=completion_semantic,
                            datacheck_type="with_datacheck",
                            memory_type=memory_type,
                            warmup_iteration_type=warmup_iteration_type)
    test.run()