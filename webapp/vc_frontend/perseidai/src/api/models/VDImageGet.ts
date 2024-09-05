/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VDModelEnum } from './VDModelEnum';
export type VDImageGet = {
    /**
     * The unique code for the image
     */
    code: string;
    /**
     * The ML model for detecting vehicles
     *
     * * `YOLOv5s` - YOLOV5S
     * * `YOLOv8s` - YOLOV8S
     */
    model?: VDModelEnum;
    /**
     * The uploaded image
     */
    image: string;
    /**
     * The inference time for the model
     */
    inf_time?: number;
    /**
     * The dictionary containing the count of each label
     */
    label_count_dict?: any;
};

